from rest_framework import  serializers
from core_app_root.security.user.models import UserProfileSummary
# class UserProfileSummarySerializer(serializers.ModelSerializer):
    # class Meta:
    #     model=UserProfileSummary
    #     fields=['interested_in','language','age_range','amount_of_apple_range','travel_mode_on','distance_range','interests']
class UserProfileSummarySerializer(serializers.ModelSerializer):
    interested_in = serializers.CharField(
        help_text="Specify the interests of the user (e.g., 'sports, reading')."
    )
    language = serializers.CharField(
        help_text="Language preference of the user (e.g., 'English')."
    )
    age_range = serializers.CharField(
        help_text="Specify age range as 'min_age-max_age' (e.g., '18-30').",
        default="18-30",
    
    )
    amount_of_apple_range = serializers.CharField(
        help_text="Specify the apple range as 'min_apple-max_apple' (e.g., '10-100').",
        default="10-100",
      
    )
    travel_mode_on = serializers.BooleanField(
        help_text="Indicate if travel mode is on (True/False).",
        default=False,
  
    )
    distance_range = serializers.CharField(
        help_text="Specify distance range in km (e.g., '0-100').",
        default="0-100",
       
    )
    interests = serializers.CharField(
        help_text="Comma-separated list of user interests (e.g., 'hiking, coding, music')."
    )

    class Meta:
        model = UserProfileSummary
        fields = ['interested_in', 'language', 'age_range', 'amount_of_apple_range', 'travel_mode_on', 'distance_range', 'interests']