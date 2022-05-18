from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.core.validators import RegexValidator
from django.db import models

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, phone, password=None, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phone:
            raise ValueError('The given phone must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password=None, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # phone = PhoneNumberField(max_length=14, unique=True, verbose_name='Phone Number', blank=False, help_text='Enter 10 digits phone number')
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=False, verbose_name='Phone Number', unique=True)
    first_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250, blank=True)
    email = models.EmailField(max_length=250, blank=True)
    national_code = models.CharField(max_length=250, blank=True)
    birth_date = models.DateField(null=True)
    GENDER_CHOICES = [
        (0, 'Undefined'),
        (1, 'Male'),
        (2, 'Female'),
    ]
    gender = models.PositiveIntegerField(null=True, choices=GENDER_CHOICES)
    NATIONALITY_CHOICES = [
        ('Iranian', 'Iranian'),
        ('Foreigner', 'Foreigner'),
    ]
    nationality = models.CharField(max_length=250, null=True, choices=NATIONALITY_CHOICES)
    notification_token = models.CharField(max_length=250, blank=True)
    OS_CHOICES = [
        ('Mac', 'Mac'),
        ('Windows', 'Windows'),
        ('Linux', 'Linux'),
        ('Android', 'Android'),
        ('Ios', 'Ios'),
    ]
    os_type = models.CharField(max_length=250, null=True, choices=OS_CHOICES)
    device_unique_id = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.phone)
