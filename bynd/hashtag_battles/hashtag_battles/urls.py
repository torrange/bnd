from django.conf.urls import include, url
from django.contrib import admin
from battleadmin.api import BattleResource

battle_resource = BattleResource()

urlpatterns = [
    url(r'^battles/', include('battleadmin.urls')),
    url(r'^api/', include(battle_resource.urls)),
    url(r'^admin/', admin.site.urls),
]
