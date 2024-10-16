from django.urls import path
from rest_framework import routers
from core_app_root.security.user.viewsets.user import UserViewset
from core_app_root.security.user.viewsets.onboarding import OnboardingUserViewset
from core_app_root.security.user.viewsets.phone_number_verification import OtpVerficationViewset,PhoneNumberModelViewset,ResendOtpViewset
from rest_framework.routers import SimpleRouter
from core_app_root.security.user.viewsets.user import UserViewset
from core_app_root.security.user.viewsets.user_summary_details import UserProfileSummaryViewset

router = SimpleRouter()

# Register the user viewset
router.register(r'user', UserViewset, basename='user')
# router.register(r'user/summary', UserProfileSummaryViewset, basename='user_sumary')


# Register the onboarding viewset with a different base URL to avoid conflicts
# router.register(r'onboarding', OnboardingUserViewset, basename='onboarding_user')

router.register(r'otp_phone_verification', PhoneNumberModelViewset, basename='otp_phone_verification')
router.register(r'otp_resend', ResendOtpViewset, basename='otp_resend')


router.register(r'otp_confirmation', OtpVerficationViewset, basename='otp_confirmation')
router.register(r'filter_users', UserProfileSummaryViewset, basename='filter_users')


# urlpatterns = [
#     *router.urls,
# ]


urlpatterns = [
    *router.urls,
    path('onboarding/<str:user__email>/', OnboardingUserViewset.as_view({'get': 'retrieve'}), name='onboarding-user-detail'),
    path('onboarding/', OnboardingUserViewset.as_view({'get': 'list', 'post': 'create'}), name='onboarding-user-list'),
]