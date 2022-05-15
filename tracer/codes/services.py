import grpc
from django_grpc_framework.services import Service
from django.contrib.auth import authenticate, login


class AuthService(Service):

    def auth_view(self, request):
        if request.method == 'Post':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:




