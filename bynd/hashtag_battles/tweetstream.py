from battleadmin.models import Battle
from battleadmin.models import Hashtag
from twitter import *
from bayespell import *


battles = queryset = Battle.objects.all()
hashtags = Hashtag.objects.all()
print hashtags

auth = OAuth("722577635939889152-R5qyydnehjWRd9ZFwmK3K5PZEjg6MC3", 
    "Ig4EC87EzQxilIhedGUKM7jPZleUmJLFc0bHnJuuAjnfK",
    "pPCXeAvd9wv5WP9WlA1h52fWd",
    "62us2GYwyUniV9TtDavbTdlCjS3nw22N8bCiN41UwrnDGEc7iX")

t = Twitter(auth=auth)

