from asyncio.proactor_events import _ProactorDuplexPipeTransport
from operator import truediv
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth import models as auth_models


# Create your models here.

class UserManager(auth_models.BaseUserManager):

    def create_user(self, phone_number: int, first_name: str, last_name: str, email: str, password: str= None, is_staff=False, is_superuser=False) -> "User":
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have first_name")
        if not last_name:
            raise ValueError("User must have an last_name")
        if not phone_number:
            raise ValueError("User must have phone_number")



        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user



    def create_superuser(self, phone_number: int, first_name: str, last_name: str, email: str, password: str= None, is_staff=False, is_superuser=False) -> "User":

        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        user.save()

        return user




class User(auth_models.AbstractUser):
    phone_number = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    objects = UserManager( )


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number", "first_name", "last_name", "password"]

