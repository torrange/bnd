from django.http import HttpResponse
from django.template import Template
from django.shortcuts import render
from battleadmin.models import Battle
from battleadmin.api import BattleResource
from twitter import *


def index(request):
    battles = [b for b in Battle.objects.all()]
    #res = BattleResource()
    #battles_api = res.obj_get_list()
    return render(request, 'battles.html', dict(battles=battles))
