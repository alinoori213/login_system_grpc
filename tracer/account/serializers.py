from django_grpc_framework import proto_serializers
from .models import UserBase
import account_pb2


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = UserBase
        proto_class = account_pb2.UserBase
        fields = ['email', 'username', 'name']
