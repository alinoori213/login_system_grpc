import grpc
from django_grpc_framework.services import Service
from .models import CustomUser
from proto import auth_pb2
from tracer.settings import TOKEN_EXPIRATION, JWT_SECRET
import datetime
import grpc
import jwt
from rest_framework_simplejwt.views import TokenObtainPairView
import ryca_django_grpc.generics as generics
from .serializers import UserProtoSerializer


class UserService(generics.ModelService):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserProtoSerializer


def generate_token(user):
    user_info = {'phone': user.phone,
                 'email': None,
                 'is_superuser': user.is_superuser,
                 'user_id': user.id
                 }
    return jwt.encode({'user_info': user_info,
                       'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=TOKEN_EXPIRATION)
                       }, JWT_SECRET, algorithm='HS256')


class LoginService(generics.ModelService, TokenObtainPairView):

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
            return response
        except Exception as e:
            return grpc.StatusCode.UNAUTHENTICATED
