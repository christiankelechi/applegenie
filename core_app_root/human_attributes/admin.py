from django.contrib import admin
from core_app_root.human_attributes import models
# Register your models here.
admin.site.register(models.HumanQualities)
admin.site.register(models.HumanInterests)