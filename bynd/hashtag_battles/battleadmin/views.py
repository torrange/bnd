from django.http import HttpResponse
from django.template import Template
from django.shortcuts import render
from battleadmin.models import Battle

def index(request):
    battles = [b for b in Battle.objects.all()]
    return render(request, 'battles.html', battles=battles)
