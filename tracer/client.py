import grpc
from google.protobuf import json_format
import auth_pb2
import auth_pb2_grpc
from django.contrib.auth.models import User

with grpc.insecure_channel('localhost:50053') as channel:
    stub = auth_pb2_grpc.AuthenticationStub(channel)
    request = auth_pb2.Create( )
    response = stub.Authentication(request)



# class AuthenticationClient(object):
#     def __init__(self, host='localhost:50053'):
#
#         self.channel = grpc.insecure_channel(host)
#         stub = auth_pb2_grpc.AuthenticationStub(self.channel)
#         self._stub = stub
#
#     def login(self, username, password):
#         request = auth_pb2.Auth(username=username, password=password)
#         response = self._stub.Authentication(request)
#         return json_format.MessageToDict(response, including_default_value_fields=True,
#                                          preserving_proto_field_name=True)
#
# a = AuthenticationClient()
# a.login('plumpi', 'new.admin.')