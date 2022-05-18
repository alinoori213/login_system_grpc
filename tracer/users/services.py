import grpc
from django.http import HttpRequest
from django_grpc_framework.services import Service
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from proto import auth_pb2
from tracer.settings import TOKEN_EXPIRATION, JWT_SECRET
import datetime
import grpc
import jwt
from rest_framework_simplejwt.views import TokenObtainPairView
import ryca_django_grpc.generics as generics
from .serializers import UserProtoSerializer, RegisterSerializer, RegistrationSerializer, CodeSerializer
from django.contrib.auth import authenticate, login


class UserService(generics.ModelService):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserProtoSerializer


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


class LoginService(generics.ModelService, TokenObtainPairView):
    # permission_classes = (IsAuthenticated,)

    def CheckUser(self, request, context):
        try:
            from google.protobuf import message

            response = auth_pb2.CheckUserResponse()
            phone = request.phone
            user = CustomUser.objects.get(phone=phone)
            print(user.pk)
            if user:
                token = generate_token(user)
                response.status == 0
                response.token = token
                # self.LoginCode(request)
                return response
            else:
                # self.Signup(request)
                response.status = grpc.StatusCode.UNAUTHENTICATED

        except Exception as e:
            return grpc.StatusCode.UNAUTHENTICATED

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

                # user = authenticate(phone, password)
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
            code = token['user_info']['user_code']
            print(token['user_info']['phone'])
            # user = CustomUser.objects.get(phone=phone)
            # print(user)

            # password = user.password
            # print(get_h)
            # user1 = authenticate(phone, password)
            # print(user1)
            # print(password)
            # print(HttpRequest.META)
            if request.code == str(code):
                # message_str = 'logged in'

                response.status == 0
                return response

                # login(request, token)

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

    # def SignupCode(self, request, context):
    #     try:
    #         from  google.protobuf import  message
    #         response = auth_pb2.SignupCodeResponse()
    #
    #
    # def ResetPasswordCheck(self, request, context):
    #     pass
    #
    # def ResetPasswordConfirm(self, request, context):
    #     pass
