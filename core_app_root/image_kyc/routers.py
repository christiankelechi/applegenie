from rest_framework import routers
from core_app_root.image_kyc.viewsets.image_kyc_viewset import UserImageKycViewset

router=routers.SimpleRouter()


router.register(r'kyc/image/verification',UserImageKycViewset,basename='kyc_image_verification')






urlpatterns=[
    *router.urls
]
