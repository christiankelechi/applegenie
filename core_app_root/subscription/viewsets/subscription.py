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
from core_app_root.subscription.models import Subscription
from core_app_root.subscription.serializers.subscription import SubscriptionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class=SubscriptionSerializer
    http_method_names=['post']
    permission_classes=[IsAuthenticated]

    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                return Response({"status":True,"redirect_url":"https://aigenie.applematch.com/checkout/","message":"You will be redirected to where to make your payment","data":serializer.data})

        except:
            return Response({"status":False,"message":"Internal server error,try again later","data":serializer.data})

        