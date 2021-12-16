from django.contrib import admin
from accounts.models import AccountUser
from adoptions.models import Pet

admin.site.register(AccountUser)
admin.site.register(Pet)
