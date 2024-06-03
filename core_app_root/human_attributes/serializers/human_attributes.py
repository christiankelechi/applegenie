from rest_framework import serializers
from core_app_root.human_attributes import models
class HumanAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=models.HumanQualities