from rest_framework import serializers
from core_app_root.security.user.models import OnboardingUserDetails

class OnboardingUserSerializer(serializers.ModelSerializer):

    class Meta:
        model=OnboardingUserDetails
        fields=['home_town','education','bio','interests','gender','primary_interest','height','opening_move','dob','values','habits','family_planning','beliefs','communities','name','current_location','language','preference','region']  

# class OTPVerificationSerializer(serializers.Serializer):
#     phone = serializers.CharField(max_length=15)
#     otp = serializers.CharField(max_length=6)
