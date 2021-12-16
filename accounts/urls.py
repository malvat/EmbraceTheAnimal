from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('sign-in', views.sign_in, name="sign_in"),
    path('sign-up', views.sign_up, name="sign_up"),
    path('sign-out', views.sign_out, name="sign_out"),
]