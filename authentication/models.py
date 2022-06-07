from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class CustumUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Vous devez fourni un email")

        email=self.normalize_email(email)
        new_user=self.model(email=email,**extra_fields)
        new_user.set_password(password)
        new_user.save()
        return new_user


    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user doit avoir is_staff True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user doit avoir is_superuser True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user doit avoir is_active True')

        return self.create_user(email,password,**extra_fields)

class User(AbstractUser):
    username = models.CharField(max_length=25,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    phone_number=PhoneNumberField(null=False,unique=True)

    USERNAME_FIELD ='email'

    REQUIRED_FIELDS = ["username","phone_number"]

    objects=CustumUserManager()

    def __str__(self):
        return f"<User {self.email}>"

