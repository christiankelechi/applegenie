from rest_framework import routers
from core_app_root.apple_gifting.viewsets import apple_gifting
router=routers.SimpleRouter()
router.register(r'apple_gifting',apple_gifting.AppleGiftingViewset,basename='apple_gifting')


urlpatterns=[
    *router.urls
]
