from django.http import HttpResponse
from django.template import Template
from django.shortcuts import render
from battleadmin.models import Battle
from battleadmin.api import BattleResource

def index(request):
    battles = [b for b in Battle.objects.all()]
    res = BattleResource()
    battles_api = [ b for b in res.obj_get_list(res)]
    return render(request, 'battles.html', dict(battles=battles_api))
