from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BLANK_CHOICE_DASH

class AccountUser(User):
    pets_posted = models.CharField(max_length=300, blank=True)
