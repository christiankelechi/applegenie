from core_app_root.match_friends.models import MatchedFriend
from rest_framework import serializers

class MatchedFriendSerializer(serializers.ModelSerializer):
    class Meta:
        model=MatchedFriend
        fields=['user_email','user_partner_email']