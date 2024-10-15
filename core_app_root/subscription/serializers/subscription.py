# serializers.py
from rest_framework import serializers
from djstripe.models import Subscription
from django.contrib.auth import get_user_model

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'status', 'current_period_start', 'current_period_end', 'customer', 'plan']  # Adjust fields as needed

# You can also serialize user data if needed
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']
