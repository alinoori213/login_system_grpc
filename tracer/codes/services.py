import grpc
from django_grpc_framework.services import Service
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import auth_pb2
import auth_pb2_grpc
from django_grpc_framework import generics
from users.models import CustomUser

# class MYServicer(auth_pb2_grpc.AuthenticationServicer):
#
#     def Login(self, request, context):
#         request = auth_pb2.Auth(username='plumpi', password='new.admin.')
#         username = request.username
#         password = request.password
#         user = authenticate(request, username=username, password=password)
#         response = auth_pb2.Auth(request)
#         if user is not None:
#             request.session['pk'] = user.pk
#         return response


# class AuthService(generics.ModelService):
#
#     queryset = CustomUser.objects.all()
#
#     def auth_view(self, request):
#         if request.method == 'Post':
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 request.session['pk'] = user.pk
#                 return user.pk, grpc.StatusCode.OK
#

    # def verify_view(self, request):
    #
    #     pk = request.session.get('pk')
    #     if pk:
    #         user = CustomUser.objects.get(pk=pk)
    #         code = user.code
    #         code_user = f"{user.username}: {user.code}"
    #         if not request.POST:
    #             print(code_user)
    #
    #             num = form.cleaned_data.get('number')
    #             if str(code) == num:
    #                 code.save()
    #                 login(request, user)
    #                 return redirect('home-view')
    #             else:
    #                 return redirect('login-view')
    #
    #         return render(request, 'verify.html', {'form': form})

