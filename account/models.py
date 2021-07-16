from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from config.validators import PhoneValidator
import re


class UserManager(BaseUserManager):
    def _create_user(self, username, password, **kwargs):
        username = PhoneValidator.clean(username)
        user = User(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, **kwargs):
        kwargs.setdefault('is_superuser', False)
        return self._create_user(**kwargs)

    def create_superuser(self, **kwargs):
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(**kwargs)


class User(AbstractUser):
    """
    Foydalanuvchilar
    """
    objects = UserManager()


    @property
    def perms(self):
        return self.get_user_permissions()

    class Meta:
        db_table = 'auth_user'

