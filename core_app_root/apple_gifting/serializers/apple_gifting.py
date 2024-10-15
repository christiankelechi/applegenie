from rest_framework import serializers
from core_app_root.security.user import models
class AppleGiftingSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=models.AppleGiftingModel