from rest_framework import serializers

from core_app_root.home_management.models import HomeManagementView
class HomeManagementSerializer(serializers.ModelSerializer):
    starting_number_range=serializers.IntegerField()
    ending_number_range=serializers.IntegerField()

    class Meta:
        model=HomeManagementView
        fields=['starting_number_range','ending_number_range']

    
    # 