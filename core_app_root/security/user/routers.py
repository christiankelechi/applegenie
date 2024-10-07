from rest_framework import routers
from core_app_root.security.user.viewsets.user import UserViewset
from core_app_root.security.user.viewsets.onboarding import OnboardingUserViewset

from rest_framework.routers import SimpleRouter
from core_app_root.security.user.viewsets.user import UserViewset

router = SimpleRouter()

# Register the user viewset
router.register(r'user', UserViewset, basename='user')

# Register the onboarding viewset with a different base URL to avoid conflicts
router.register(r'onboarding', OnboardingUserViewset, basename='onboarding_user')

urlpatterns = [
    *router.urls,
]

