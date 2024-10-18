# serializers.py
from rest_framework import serializers
from core_app_root.subscription.models  import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields=['click_subscription']
      
