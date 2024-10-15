from rest_framework import serializers
from core_app_root.security.user.models import User,PasswordChangeModel,PasswordResetModel
class PasswordUpdateSerializer(serializers.ModelSerializer):
    # old_password=serializers.CharField(max_length=20)
    # final_password=serializers.CharField(max_length=20)
    # repeat_final_password=serializers.CharField(max_length=20)
    email=serializers.CharField(max_length=1000)
    class Meta:
        model=PasswordChangeModel
        fields='__all__'

class ResetPasswordSerializer(serializers.ModelSerializer):
    email=serializers.CharField(max_length=1000)
    # final_password=serializers.CharField(max_length=20)
    # repeat_final_password=serializers.CharField(max_length=20)
    class Meta:
        model=PasswordResetModel
        fields='__all__'
        
    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidatorError("No user is associated with this email")            
        return value
    
class ResetPasswordConfirmSerializer(serializers.ModelSerializer):
    # previous_password = serializers.CharFi
    pass