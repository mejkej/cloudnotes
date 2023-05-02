from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager
from django.validators import MinLengthValidator
from django.db import models
class UserManager(DefaultUserManager):
    pass

class CustomUser(AbstractUser):

    objects = UserManager()
    username = models.CharField(max_length=20, unique=True, validators=[MinLengthValidator(3)])