from rest_framework import serializers
from core_app_root.security.user.models import OnboardingUserDetails

class OnboardingUserSerializer(serializers.ModelSerializer):

    class Meta:
        model=OnboardingUserDetails
        fields="__all__"  