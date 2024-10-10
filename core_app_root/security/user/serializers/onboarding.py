from rest_framework import serializers
from core_app_root.security.user.models import OnboardingUserDetails

class OnboardingUserSerializer(serializers.ModelSerializer):

    class Meta:
        model=OnboardingUserDetails
        fields=['interests','gender','primary_interest','height','opening_move','dob','values','habits','family_planning','beliefs','communities','name','phone','current_location','language','preference','region']  
 
    