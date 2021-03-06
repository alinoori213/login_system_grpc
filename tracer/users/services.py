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
from codes.models import Code
from .serializers import UserProtoSerializer, RegisterSerializer, RegistrationSerializer, CodeSerializer
from django.contrib.auth import authenticate, login
import os
import random
from twilio.rest import Client


def generate_sms_code(user):
    number_list = [x for x in range(10)]
    code_items = []
    for i in range(5):
        num = random.choice(number_list)
        code_items.append(num)

    code_string = "".join(str(item) for item in code_items)
    code = Code.objects.get(user=user)
    code.number = code_string
    code.save()
    return code


def send_forgot_mail(phone):
    user = CustomUser.objects.get(phone=phone)
    code = user.code
    subject = 'confirmation code'
    message = f' please confirm the code \n your code is : {code} '
    email_from = 'tracer@gmail.com'
    email = [user.email]
    send_mail(subject, message, email_from, email)


def generate_token(user):
    generate_sms_code(user)

    user_info = {'phone': user.phone,
                 'is_superuser': user.is_superuser,
                 'email': user.email,
                 'user_id': user.id,
                 'user_code': user.code.number
                 }
    return jwt.encode({'user_info': user_info,
                       'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=TOKEN_EXPIRATION)
                       }, JWT_SECRET, algorithm='HS256'), user.code.number


def send_sms(phone):
    user = CustomUser.objects.get(phone=phone)
    code = user.code
    account_sid = 'ACe3e60c6f3c8077fde0c26f8e7dc548f4'
    auth_token = 'c5c9acb15e237c0d61be1e99c228274e'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f'here is your code : {code}',
        from_='+18562494313',
        to = phone
    )
    print(message.sid)


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
                print(token[1])
                response.status == 0

                # sms = int(token['user_info']['user_code'])
                # print(sms)
                response.token = token[0]

                return response
            except CustomUser.DoesNotExist:
                 response.status == 0
                 user = CustomUser.objects.create(phone=phone)
                 newtoken = generate_token(user)
                 response.token = newtoken[0]
                 pm = 'your phone number has submited'
                 # sms = generate_sms_code(user)
                 print(newtoken[1])
                 return response
            else:
                response.status = grpc.StatusCode.UNAUTHENTICATED

    def Login(self, request, context):
        try:
            from google.protobuf import message
            response = auth_pb2.LoginResponse()
            phone = request.phone
            print(phone)
            password = request.password
            print(password)
            user = CustomUser.objects.get(phone=phone)

            valid = user.check_password(password)
            print(valid)
            if valid:
                token = generate_token(user)
                print(token)
                response.token = token[0]
                print(response)
                return response

            else:
                response.status = grpc.StatusCode.UNAUTHENTICATED
            return response
        except Exception as e:
            return grpc.StatusCode.UNAUTHENTICATED

    def LoginCode(self, request, context):
        try:

            from google.protobuf import message
            response = auth_pb2.LoginCodeResponse()
            # serializer = CodeSerializer(code=request.code)
            # serializer.is_valid()
            token = request.token
            str_token = jwt.decode(token, JWT_SECRET, algorithms='HS256')
            code = str_token['user_info']['user_code']
            print(request.code, '    ', code)
            if int(request.code) == int(code):
                response.status == 0
                return response
            else:
                response.status = grpc.StatusCode.UNAUTHENTICATED
            return response
        except Exception as e:
            return grpc.StatusCode.UNAUTHENTICATED

    def Signup(self, request, context):

        #add password serializer to hash password
        try:
            from google.protobuf import message
            response = auth_pb2.SignupResponse()
            phone = request.phone
            email = request.email
            if request.password == request.password2:
                password = request.password
                user = CustomUser.objects.create(phone=phone, password=password, email=email)
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
        user_code = int(token['user_info']['user_code'])
        code = int(request.code)
        print(code, type(code))
        print(type(user_code), user_code)
        print(user_code == code)
        if code == user_code:
            response.status == 0
            return response

    def ResetPasswordCheck(self, request, context):
        response = auth_pb2.ResetPasswordCheckResponse()
        phone = request.phone
        send_forgot_mail(phone)
        user = CustomUser.objects.get(phone=phone)
        token = generate_token(user)
        email = user.email
        reformed_email = email[0] + '******@' + email.split("@", 1)[1]
        message = 'code sent'
        response.message = message
        response.email = reformed_email
        response.token = token
        return response


    def ResetPasswordConfirm(self, request, context):
        response = auth_pb2.ResetPasswordConfirmResponse()
        code = request.code
        password = request.password
        password1 = request.password
        if password == password1:
            token = request.token
            token = jwt.decode(token, JWT_SECRET, algorithms='HS256')
            user_code = str(token['user_info']['user_code'])
            phone = str(token['user_info']['phone'])
            user = CustomUser.objects.get(phone=phone)
            user.password = password
            user.save()
        else:
            return 'password does not match'
        if code == user_code:
            return response
        else:
            response.status = grpc.StatusCode.UNAUTHENTICATED
        return response