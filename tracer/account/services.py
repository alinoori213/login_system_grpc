from .models import UserBase
from django_grpc_framework import generics
from .serializers import UserProtoSerializer


class UserService(generics.ModelService):

    queryset = UserBase.objects.all()
    serializer_class = UserProtoSerializer