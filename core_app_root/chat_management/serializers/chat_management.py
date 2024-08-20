from rest_framework import serializers
from core_app_root.chat_management import models
class ChatManagement(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=models.ChatClientModel

class StoreUserChatSerializer(serializers.ModelSerializer):
    class Meta:
        fields=['email','suggestion_question','user_response']
        model=models.StoreUserChatModel

class UserQuestionsHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.UserQuestions
        fields=['email']

class GenieQuestionsHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.GenieQuestions
        fields=['email']

class UserResponseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.UserResponseToGenie
        fields=['email']

class GenieResponseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.GenieResponseToUser
        fields=['email']