from rest_framework import serializers
from core_app_root.chat_management import models
class ChatManagement(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=models.ChatClientModel

class StoreUserChatSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=models.StoreUserChatModel
    # 