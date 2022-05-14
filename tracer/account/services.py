from .models import UserBase
from django_grpc_framework import generics
from .serializers import UserProtoSerializer
import datetime

import grpc
import jwt
from rest_framework_simplejwt.views import TokenObtainPairView
from django_grpc_framework import generics

from .authenticate import IsAuthenticated
from .models import UserBase
from .serializers import UserProtoSerializer
import account_pb2
import auth_pb2

from tracer.settings import TOKEN_EXPIRATION, JWT_SECRET


class UserService(generics.ModelService):

    queryset = UserBase.objects.all()
    serializer_class = UserProtoSerializer


def generate_token(user):
    user_info = {'user_name': user.user_name,
                 'email': user.email,
                 'is_superuser': user.is_superuser,
                 'user_id': user.id
                 }
    return jwt.encode({'user_info': user_info,
                       'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=TOKEN_EXPIRATION)
                       }, JWT_SECRET, algorithm='HS256')


class LoginService(generics.ModelService):


    def LoginUser(self, request):

        email = request.email
        print(email)
        password = request.password
        print(password)
        user = UserBase.objects.get(email=email)
        valid = user.check_password(password)
        response = auth_pb2.LoginResponse()

        if valid:
            token = generate_token(user)
            response.token = token
        else:
            response.status = grpc.StatusCode.UNAUTHENTICATED
        return response


