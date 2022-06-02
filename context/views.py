
import os
import requests
import sys
import operator
import math
import re
import unicodedata
import string






# Django SIDE
import json
from subprocess import run, PIPE  # running files
from django.http import HttpResponse
from django.utils.translation import gettext

from .models import Contexte
from .serializers import ContexteSerializer

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.contrib.auth.models import User
# Application SIDE
import datetime
import pandas as pd

data= pd.read_csv('base_synda-Feuille-1.csv')

etiquettes = data['context'].values.tolist()
print(etiquettes)
textes = data['Text'].values.tolist()
keywords1 = data['keywords'].values.tolist()

@csrf_exempt
def lda(request):
    global keywords1
    # retrieve values from db


    if request.method == 'POST':
        # parsing input
        print("1*Parsing Input")
        text_data = JSONParser().parse(request)
        inp = text_data['text']
        txt = str(inp)
        id_user = str(text_data['id_user'])
        id_user = int(id_user)
        #user = User.objects.get(pk=id_user)
        pos=0

        for i in range(len(textes)):

            if textes[i] == txt:
                print(txt)
                print(textes[i])
                pos = i
        print(pos)
        sim=etiquettes[pos]
        print(sim)
     #   new_contexte = Contexte(etiquette=sim)
     #   new_contexte.save()
        #context=sim
        # serialize the context to be sent to front-end
       # context_serialized = ContexteSerializer(context)
      #  print(" Context is", context_serialized.data)
        json_result = json.dumps(
            {'context': sim, 'keywords': ""})
        return HttpResponse(json_result)