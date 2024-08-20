from rest_framework import serializers
from core_app_root.human_attributes import models
class HumanAttributesSerializer(serializers.ModelSerializer):
    age=serializers.CharField()
    
    # class Meta:
    #     fields="__all__"
    #     model=models.HumanQualities

class HumanInterestSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=models.HumanInterests