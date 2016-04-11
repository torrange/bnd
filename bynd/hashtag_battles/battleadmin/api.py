from tastypie.resources import ModelResource
from battleadmin.models import Battle
from battleadmin.models import Hashtag


class BattleResource(ModelResource):
    class Meta:
        queryset = Battle.objects.all()
        resource_name = 'battle'


class HashtagResource(ModelResource):
    class Meta:
        queryset = Hashtag.objects.all()
        resource_name = 'hashtag'

