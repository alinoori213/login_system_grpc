"""tracer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from codes.views import home_view, auth_view, verify_view
# import account_pb2_grpc
# import auth_pb2_grpc
# from account.services import UserService, LoginService


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home-view'),
    path('login/', auth_view, name='auth-view'),
    path('verify/', verify_view, name='verify-view')
    # path('account/', include('account.urls', namespace='account')),
    # path('api/v1/', include('core.api.urls')),

]


# def grpc_handlers(server):
#     account_pb2_grpc.add_UserBaseControllerServicer_to_server(UserService.as_servicer(), server)
#     auth_pb2_grpc.add_AuthenticationServicer_to_server(LoginService.as_servicer(), server)