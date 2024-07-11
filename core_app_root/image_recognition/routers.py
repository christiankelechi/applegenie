from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core_app_root.image_recognition.viewsets.image_recognizer import PhotoViewSet

router = DefaultRouter()
router.register(r'photos', PhotoViewSet)
# router.register(r'tags', TagViewSet)

urlpatterns=[
    *router.urls
]