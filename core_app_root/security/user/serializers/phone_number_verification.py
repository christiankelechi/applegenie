from rest_framework import serializers
from core_app_root.security.user.models import PhoneNumbersModel
from rest_framework import serializers
class ResendOtpSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    
    class Meta:
        fields=['phone']
    


class PhoneNumberModelSerializer(serializers.ModelSerializer):

    class Meta:
        model=PhoneNumbersModel
        fields=["phone"]  

class OTPVerificationSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    code = serializers.CharField(max_length=6)

