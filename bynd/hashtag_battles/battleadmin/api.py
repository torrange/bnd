from tastypie.resources import ModelResource
from battleadmin.models import Battle
from battleadmin.models import Hashtag


class BattleResource(ModelResource):
    class Meta:
        queryset = Battle.objects.all()
        resource_name = 'battle'

    def dehydrate(self, bundle):
        bundle.data['winner'] = bundle.obj.hwinr()
        bundle.data['h1tag'] = bundle.obj.h1tag()
        bundle.data['h2tag'] = bundle.obj.h2tag()
        return bundle


class HashtagResource(ModelResource):
    class Meta:
        queryset = Hashtag.objects.all()
        resource_name = 'hashtag'

