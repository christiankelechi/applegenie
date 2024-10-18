from django.contrib import admin
from core_app_root.security.user.models import User,OnboardingUserDetails,PhoneNumbersModel,UserProfileSummary,AppleGiftingModel,AppleRecievedNotificationDashboard,AppleSentDashbaord
# Register your models here.

admin.site.register(User)
# admin.site.register(Image)
admin.site.register(OnboardingUserDetails)
admin.site.register(PhoneNumbersModel)
admin.site.register(UserProfileSummary)
admin.site.register(AppleRecievedNotificationDashboard)
admin.site.register(AppleGiftingModel)
admin.site.register(AppleSentDashbaord)