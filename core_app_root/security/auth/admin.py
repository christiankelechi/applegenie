from django.contrib import admin
from core_app_root.security.auth.models import GoogleSignInModel,GoogleLoginModel
# Register your models here.
admin.site.register(GoogleSignInModel)
admin.site.register(GoogleLoginModel)