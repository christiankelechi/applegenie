from rest_framework import serializers
from core_app_root.apple_gifting import models
class AppleGiftingSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=models.AppleGiftingModel