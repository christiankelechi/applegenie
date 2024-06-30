from rest_framework import serializers
from core_app_root.chat_management import models
class QuestionAndAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.QuestionAndAnswer
        fields=['prompt_in']