from django.contrib import admin
from core_app_root.security.user.models import User,Image,OnboardingUserDetails
# Register your models here.

admin.site.register(User)
admin.site.register(Image)
admin.site.register(OnboardingUserDetails)