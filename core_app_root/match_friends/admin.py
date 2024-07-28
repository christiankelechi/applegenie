from django.contrib import admin
from core_app_root.match_friends import models
# Register your models here.
admin.site.register(models.UserAttributes)
admin.site.register(models.MatchFriend)
