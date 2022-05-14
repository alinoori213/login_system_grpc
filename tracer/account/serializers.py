from django_grpc_framework import proto_serializers
from rest_framework import serializers
from .models import UserBase
import account_pb2
import auth_pb2


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = UserBase
        proto_class = account_pb2.UserBase
        fields = ['email', 'username', 'name']


class UserLoginSerializer(proto_serializers.ModelProtoSerializer):

    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    class Meta:

        proto_class = auth_pb2.LoginRequest
