from statistics import mode
from django.db import models
from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser, AbstractUser
)
from django.contrib.auth.models import PermissionsMixin
# Create your models here.
class CustomUserManager(BaseUserManager):
	def create_user(self, password, first_name, phone=None, last_name=None):

		if not phone:
			raise ValueError("User must have phone number")

		user = self.model(
			first_name = first_name,
			last_name = last_name,
			phone = phone
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, password, first_name, phone=None, last_name=None):
        
		user = self.create_user(
			first_name = first_name,
			last_name = last_name,
			phone = phone,
			password = password
		)
		user.is_admin=True
        
		user.save(using=self._db)
		return user

class CustomUser(AbstractBaseUser, PermissionsMixin):

	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150,null=True)
	email = models.EmailField(null=True)
    national_code = models.CharField(max_length=10)
	phone = models.CharField(max_length=150,unique=True)
	password = models.CharField(max_length=150)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
    

	USERNAME_FIELD = 'phone'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	objects = CustomUserManager()

	def __str__(self):
		return "{} {}".format(self.phone, self.first_name)

	@property
	def is_staff(self):
		return self.is_admin

	@property
	def is_anonymous(self):
		return False

	@property
	def is_authenticated(self):
		return True

	class Meta():
		db_table = 'auth_user'
		verbose_name = 'User'
		verbose_name_plural = 'Users'