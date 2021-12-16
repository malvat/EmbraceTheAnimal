from django.contrib import admin
from django.urls import path
from adoptions import views

urlpatterns = [
    path('add-new-pet', views.add_new_pet, name="add_new_pet"),
]