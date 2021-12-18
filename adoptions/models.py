from io import BufferedReader
from django.db import models
from django.db.models.base import ModelState
from django.db.models.fields import BLANK_CHOICE_DASH
from accounts.models import AccountUser

class Pet(models.Model): 
    GENDER_CHOICES = {
        ('M', 'Male'),
        ('F', 'Female'),
    }
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(blank=False)
    species = models.CharField(max_length=100, blank=False)
    breed = models.CharField(max_length=100, blank=False)
    weight =  models.IntegerField(blank=False)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    hobbies = models.CharField(max_length=100, blank=False)
    summary = models.CharField(max_length=500, blank=False)
    submitter = models.ForeignKey(AccountUser, on_delete=models.CASCADE, default="1")
    profile_pic = models.ImageField(null=True, blank=True)