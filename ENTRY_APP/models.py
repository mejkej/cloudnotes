from django.db import models
from django.contrib.auth.models import AbstractUser, UserCreationForm, AuthenticationForm
from django.contrib.auth import login
class User(AbstractUser):
    pass
