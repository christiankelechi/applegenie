from django.contrib import admin
from core_app_root.security.user import models
# Register your models here.
admin.site.register(models.AppleGiftingModel)
admin.site.register(models.AppleModel)