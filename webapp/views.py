from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

def home(request):
    s = requests.get('https://disease.sh/v3/covid-19/countries')
    countries = s.json()
    return render(request, 'webapp/home.html', {'countries':countries})


    
    
