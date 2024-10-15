from rest_framework import  serializers
from core_app_root.security.user.models import UserProfileSummary
class UserProfileSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfileSummary
        fields="__all__"