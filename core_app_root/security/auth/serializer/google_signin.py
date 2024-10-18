from rest_framework import serializers
from core_app_root.security.auth.models import GoogleSignInModel,GoogleLoginModel
class GoogleSignInSerializer(serializers.ModelSerializer):
    class Meta:
        model=GoogleSignInModel
        fields=['user_id','name','email']

class GoogleLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=GoogleLoginModel
        fields=['email']