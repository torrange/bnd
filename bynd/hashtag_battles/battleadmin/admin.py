from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from tastypie.admin import ApiKeyInline
from .models import Battle
from .models import Hashtag


class UserModelAdmin(UserAdmin):
    inlines = UserAdmin.inlines + [ApiKeyInline]


admin.site.unregister(User)
admin.site.register(User, UserModelAdmin)
admin.site.register(Battle)
admin.site.register(Hashtag)

