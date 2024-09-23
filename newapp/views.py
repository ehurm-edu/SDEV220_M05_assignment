from django.shortcuts import render
from django.http import HttpResponse
from newapp.models import *

# Create your views here.
def index(request): #SDEV 220
    foster_details = Fosters.objects.all()
    foster_dictionary = {'foster_key': foster_details}
    return render(request, 'index.html', context=foster_dictionary)