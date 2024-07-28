from django.contrib import admin
from core_app_root.chat_management import models
# Register your models here.
admin.site.register(models.ChatClientModel)
admin.site.register(models.StoreUserChatModel)
admin.site.register(models.UserHistory)
admin.site.register(models.UserQuestions)
admin.site.register(models.UserResponseToGenie)

admin.site.register(models.GenieQuestions)
admin.site.register(models.GenieResponseToUser)


