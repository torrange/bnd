from __future__ import unicode_literals
from django.db import models

class Hashtag(models.Model):
    tag = models.CharField(max_length=140)
    typos = models.IntegerField(default=0)
    __unicode__ = lambda self: self.tag 

class Battle(models.Model):
    battle_title = models.CharField(max_length=280)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    winner = models.CharField(max_length=140, default='Draw')
    h1 = models.ManyToManyField(Hashtag, related_name='hashtag_1')
    h2 = models.ManyToManyField(Hashtag, related_name='hashtag_2')
    h1tag = lambda self: self.h1.values()[0]['tag']
    h2tag = lambda self: self.h2.values()[0]['tag']
    h1typ = lambda self: self.h1.values()[0]['typos']
    h2typ = lambda self: self.h2.values()[0]['typos']
    hgreq = lambda self: self.h1typ() == self.h2typ()
    hcomp = lambda self: self.h1tag() if self.h1typ() < self.h2typ() else self.h2tag()
    hwinr = lambda self: 'Draw' if self.hgreq() else self.hcomp()
    __unicode__ = lambda self: self.battle_title 
