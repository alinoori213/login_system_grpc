# from django.urls import path, include
#
# urlpatterns = [
#
#     path('account/', include('account.api.urls')),
#
# ]
import grpc
import account_pb2
import account_pb2_grpc
import auth_pb2
import auth_pb2_grpc


# with grpc.insecure_channel('localhost:50051') as channel:
#     stub = account_pb2_grpc.UserBaseControllerStub(channel)
#     for user in stub.List(account_pb2.UserBaseListRequest()):
#         print(user, end='')
#

with grpc.insecure_channel('localhost:50051') as channel:

    stub = auth_pb2_grpc.AuthenticationStub(channel)
    request = auth_pb2.LoginRequest(email='ali.nouri213@gmail.com', password='new.admin.')

    # request = auth_pb2.LoginRequest(email='ali.nouri213@gmail.com', password='new.admin.')
    print(stub.Login(request).status)
