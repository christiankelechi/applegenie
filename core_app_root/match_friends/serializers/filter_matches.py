from core_app_root.match_friends.models import FilterMatches 
from rest_framework import serializers
class FilterMatchesSerializer(serializers.ModelSerializer):

    class Meta:
        model=FilterMatches
        fields="__all__"