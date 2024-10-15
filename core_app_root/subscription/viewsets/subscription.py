# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from djstripe.models import Subscription
from core_app_root.subscription.serializers.subscription import SubscriptionSerializer
from django.conf import settings
from django.contrib.auth import get_user_model
import stripe
from djstripe.settings import djstripe_settings
from core_app_root import base_url 
class CreatePortalSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY
        try:
            portal_session = stripe.billing_portal.Session.create(
                customer=request.user.customer.id,
                return_url=f"{base_url.backend_url}subscription-details/",
            )
            return Response({"url": portal_session.url}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import serializers

class SubscriptionConfirmSerializer(serializers.Serializer):
    session_id = serializers.CharField(max_length=255)

class SubscriptionConfirmView(APIView):
    permission_classes = [IsAuthenticated]
    

    def create(self, request):
        stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY
        serializer = SubscriptionConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        session_id = serializer.validated_data['session_id']

        try:
            session = stripe.checkout.Session.retrieve(session_id)
            client_reference_id = int(session.client_reference_id)
            subscription_holder = get_user_model().objects.get(id=client_reference_id)

            if subscription_holder != request.user:
                return Response({"error": "Invalid user"}, status=status.HTTP_403_FORBIDDEN)

            subscription = stripe.Subscription.retrieve(session.subscription)
            djstripe_subscription = Subscription.sync_from_stripe_data(subscription)

            subscription_holder.subscription = djstripe_subscription
            subscription_holder.customer = djstripe_subscription.customer
            subscription_holder.save()

            return Response({"message": "Subscription confirmed successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
