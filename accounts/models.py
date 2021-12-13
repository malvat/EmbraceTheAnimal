from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

class AccountUser(AbstractBaseUser):
    pets_posted = models.CharField(max_length=300, blank=True)
    password = models.CharField(max_length=300, blank=False, unique=False, default="anim1610")
    email = models.CharField(max_length=300, blank=False, unique=True)
    first_name = models.CharField(max_length=300, blank=False, default="anim")
    last_name = models.CharField(max_length=300, blank=False, default="malvat")
    
