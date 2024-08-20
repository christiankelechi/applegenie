from rest_framework import serializers
from core_app_root.image_kyc.models import UserImageKyc
class UserImageKycSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserImageKyc
        fields=['user_default_image','user_real_time_capture']