from ryca_django_grpc import proto_serializers
from rest_framework import serializers
from .models import CustomUser
from proto import user_pb2, auth_pb2


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = CustomUser
        proto_class = user_pb2.CustomUser
        fields = ['id', 'phone', 'email']


class RegisterSerializer(proto_serializers.ProtoSerializer):
    phone = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    password2 = serializers.CharField(max_length=100)

    class Meta:
        proto_class = auth_pb2.SignupResponse


class RegistrationSerializer(serializers.ModelSerializer):

	password2 = serializers.CharField(write_only=True)

	class Meta:
		model = CustomUser
		fields = ['phone', 'password', 'password2']
		extra_kwargs = {
				'password': {'write_only': True},
		}

	def	save(self):

		account = CustomUser(phone=self.validated_data['phone'],)

		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		account.set_password(password)
		account.save()
		return account


class CodeSerializer(proto_serializers.ProtoSerializer):
	code = serializers.CharField(max_length=5)