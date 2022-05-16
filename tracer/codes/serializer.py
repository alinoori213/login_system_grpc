from users.models import CustomUser
from rest_framework import serializers
from django_grpc_framework import proto_serializers
import auth_pb2


class AuthProtoSerializer(proto_serializers.ProtoSerializer):
    username = serializers.CharField(max_length=100)

    class Meta:
        proto_class = auth_pb2.Auth