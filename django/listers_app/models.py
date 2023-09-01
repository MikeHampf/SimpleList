from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_name

class Lister(AbstractUser):
    email = models.EmailField(verbose_name='email address', max_length=32, unique=True)
    user_name = models.CharField(max_length=64, null=True, validators=[validate_name])
    date_joined = models.DateField(auto_now_add=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    
