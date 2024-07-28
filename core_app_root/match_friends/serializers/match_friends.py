from core_app_root.match_friends import models
from rest_framework import serializers


        
class MatchFriendsSerializers(serializers.ModelSerializer):
    class Meta:
        fields=['user_email','user_partner_email']
        model=models.MatchFriend

class AskQuestionsToMatchSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=models.AskQuestionsToMatchModel