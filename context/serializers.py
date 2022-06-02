from rest_framework import serializers
from .models import *


class ContexteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contexte
        fields = ['etiquette']