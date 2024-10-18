from core_app_root.subscription.viewsets.subscription import SubscriptionViewSet

from rest_framework import routers
from django.urls import path
router=routers.SimpleRouter()
router.register(r'subscription',SubscriptionViewSet,basename='subscription')





urlpatterns=[
    *router.urls,

]
