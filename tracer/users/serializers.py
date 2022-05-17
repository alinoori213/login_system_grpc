from ryca_django_grpc import proto_serializers

from .models import CustomUser
from proto import user_pb2


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = CustomUser
        proto_class = user_pb2.CustomUser
        fields = ['id', 'phone', 'email']
