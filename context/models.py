from django.urls import include, path

from rest_framework import routers
from django.db import models

# Create your models here.

class Contexte(models.Model):
    etiquette = models.CharField(max_length=1000,blank=False,default='')

    def __str__(self):
        return self.etiquette

