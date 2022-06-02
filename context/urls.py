from django.urls import include, path
from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [

path('lda', views.lda),
]