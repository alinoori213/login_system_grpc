import grpc
from django.http import HttpRequest
from django_grpc_framework.services import Service
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from django.conf import settings
from proto import auth_pb2
from tracer.settings import TOKEN_EXPIRATION, JWT_SECRET
import datetime
import grpc
import jwt
from rest_framework_simplejwt.views import TokenObtainPairView
import ryca_django_grpc.generics as generics
from django.core.mail import send_mail
from .serializers import UserProtoSerializer, RegisterSerializer, RegistrationSerializer, CodeSerializer
from django.contrib.auth import authenticate, login


def send_forgot_mail(phone):
    user = CustomUser.objects.get(phone=phone)
    code = user.code
    subject = 'confirmation code'
    message = f' please confirm the code \n your code is : {code} '
    email_from = 'tracer@gmail.com'
    email = [user.email]
    send_mail(subject, message, email_from, email)


def generate_token(user):
    user_info = {'phone': user.phone,
                 'is_superuser': user.is_superuser,
                 'email': user.email,
                 'user_id': user.id,
                 'user_code': user.code.number
                 }
    return jwt.encode({'user_info': user_info,
                       'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=TOKEN_EXPIRATION)
                       }, JWT_SECRET, algorithm='HS256')


class UserService(generics.ModelService):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserProtoSerializer


class LoginService(generics.ModelService, TokenObtainPairView):
    # permission_classes = (IsAuthenticated,)

    def CheckUser(self, request, context):

            response = auth_pb2.CheckUserResponse()
            phone = request.phone

            try:
                user = CustomUser.objects.get(phone=phone)
                token = generate_token(user)
                response.status == 0
                response.token = token

                return response
            except CustomUser.DoesNotExist:
                 print('hello')
                 response.status == 0
                 user = CustomUser.objects.create(phone=phone)
                 print(user)
                 newtoken = generate_token(user)
                 response.token = newtoken
                 pm = 'your phone number has submited'
                 return response, pm

            else:
                response.status = grpc.StatusCode.UNAUTHENTICATED


    def Login(self, request, context):
        try:
            from google.protobuf import message
            response = auth_pb2.LoginResponse()
            phone = request.phone
            password = request.password
            user = CustomUser.objects.get(phone=phone)
            valid = user.check_password(password)
            if valid:
                token = generate_token(user)
                response.token = token

            else:
                response.status = grpc.StatusCode.UNAUTHENTICATED
            print(response.status)
            return response
        except Exception as e:
            return grpc.StatusCode.UNAUTHENTICATED

    def LoginCode(self, request, context):
        try:

            from google.protobuf import message
            response = auth_pb2.LoginCodeResponse()
            # serializer = CodeSerializer(code=request.code)
            # serializer.is_valid()
            print(request)
            token = request.token
            token = jwt.decode(token, JWT_SECRET, algorithms='HS256')
            code = str(token['user_info']['user_code'])
            print(token['user_info']['phone'])
            if request.code == str(code):
                response.status == 0
                return response

            else:
                response.status = grpc.StatusCode.UNAUTHENTICATED
            print(response.status)
            return response
        except Exception as e:
            return grpc.StatusCode.UNAUTHENTICATED

    def Signup(self, request, context):

        #add password serializer to hash password
        try:
            from google.protobuf import message
            response = auth_pb2.SignupResponse()
            phone = request.phone
            print(phone)
            if request.password == request.password2:
                password = request.password
                user = CustomUser.objects.create(phone=phone, password=password)
                print(user)
                token = generate_token(user)
                response.token = token
            else:
                response.status = grpc.StatusCode.UNAUTHENTICATED

            return response
        except Exception as e:
            return grpc.StatusCode.UNAUTHENTICATED

    def SignupCode(self, request, context):

        response = auth_pb2.SignupCodeResponse()
        token = request.token
        token = jwt.decode(token, JWT_SECRET, algorithms='HS256')
        user_code = token['user_info']['user_code']
        code = request.code

        if code == str(user_code):

            return response

    def ResetPasswordCheck(self, request, context):
        response = auth_pb2.ResetPasswordCheckResponse()
        phone = request.phone
        send_forgot_mail(phone)
        user = CustomUser.objects.get(phone=phone)
        token = generate_token(user)
        email = user.email
        reformed_email = email[0] + '******@' + email.split("@", 1)[1]
        print(reformed_email)
        message = 'code sent'
        response.message = message
        response.email = reformed_email
        response.token = token

        return response

    def ResetPasswordConfirm(self, request, context):
        response = auth_pb2.ResetPasswordConfirmResponse()
        code = request.code
        token = request.token
        token = jwt.decode(token, JWT_SECRET, algorithms='HS256')
        user_code = str(token['user_info']['user_code'])
        if code == user_code:
            return response
        else:
            response.status = grpc.StatusCode.UNAUTHENTICATED

        return response