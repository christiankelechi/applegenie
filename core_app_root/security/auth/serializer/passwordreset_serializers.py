from rest_framework import serializers
from core_app_root.security.user.models import User
class PasswordUpdateSerializer(serializers.ModelSerializer):
    # old_password=serializers.CharField(max_length=20)
    # final_password=serializers.CharField(max_length=20)
    # repeat_final_password=serializers.CharField(max_length=20)
    email=serializers.CharField(max_length=1000)
    class Meta:
        # model=PasswordChangeModel
        fields='__all__'

class ResetPasswordSerializer(serializers.Serializer):
    email=serializers.CharField(max_length=1000)
    # final_password=serializers.CharField(max_length=20)
    # repeat_final_password=serializers.CharField(max_length=20)
    class Meta:
        # model=PasswordResetModel
        fields='__all__'
        
    def validate_data(self, data):
        if not User.objects.filter(email=data['email']).exists():
            raise serializers.ValidatorError("No user is associated with this email")            
        return value
    
class ResetPasswordConfirmSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=255)
    new_password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255)
    
    class Meta:
        fields = "__all__"
        
    def validate_data(self, data):
        if data['new_password'] == data['confirm_password']:
            return True
        raise serializers.ValidatorError("New password is not the same as old password")