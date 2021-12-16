from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

class AccountUser(AbstractBaseUser):
    pets_posted = models.CharField(max_length=300, blank=True)
    password = models.CharField(max_length=300, blank=False, unique=False, default="anim1610")
    email = models.CharField(max_length=300, blank=False, unique=True)
    first_name = models.CharField(max_length=300, blank=False, default="anim")
    last_name = models.CharField(max_length=300, blank=False, default="malvat")

    def GetValues(self): 
        result = {}
        result['pets_posted'] = self.pets_posted
        result['email'] = self.email
        result['first_name'] = self.first_name
        result['last_name'] = self.last_name
        return result

    def __str__(self): 
        return self.first_name + " " + self.last_name
    
