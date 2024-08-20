from django.contrib import admin
from core_app_root.image_recognition.models import Photo,Tag
# Register your models here.
admin.site.register(Photo)
admin.site.register(Tag)