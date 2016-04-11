from tastypie.resources import ModelResource
from battleadmin.models import Battle
from battleadmin.models import Hashtag


class BattleResource(ModelResource):
    class Meta:
        queryset = Battle.objects.all()
        resource_name = 'battle'

    def dehydrate(self, bundle):
        bundle.data['winner'] = bundle.obj.hwinr()
        bundle.data['hashtag1'] = bundle.obj.h1tag()
        bundle.data['hashtag1_typos'] = bundle.obj.h1typ()
        bundle.data['hashtag2'] = bundle.obj.h2tag()
        bundle.data['hashtag2_typos'] = bundle.obj.h2typ()
      
        return bundle


class HashtagResource(ModelResource):
    class Meta:
        queryset = Hashtag.objects.all()
        resource_name = 'hashtag'

