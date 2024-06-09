from django.contrib import admin
from django.urls import path, include
from .views import login

urlpatterns = [
    path('v1/', login, name="login"),
]
