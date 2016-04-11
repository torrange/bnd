from django.http import HttpResponse
from django.template import Template
from django.shortcuts import render

def index(request):
    return render(request, 'battles.html')
