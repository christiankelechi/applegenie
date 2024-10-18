from core_app_root.security.auth.viewsets.password import ResetPasswordViewSet, ResetPasswordConfirmViewSet
from core_app_root.security.auth.viewsets.register import RegisterViewSet
from core_app_root.security.auth.viewsets.login import LoginViewSet
from core_app_root.security.auth.viewsets.google_signin import GoogleSignInViewSet,GoogleLoginViewSet

from rest_framework import routers
from django.urls import path
router=routers.SimpleRouter()
router.register(r'register',RegisterViewSet,basename='register')
router.register(r'login',LoginViewSet,basename='login')
router.register(r'passwordreset', ResetPasswordViewSet, basename="passwordreset")

router.register(r'register_google',GoogleSignInViewSet,basename='google_signup')
router.register(r'login_google',GoogleLoginViewSet,basename='google_login')




urlpatterns=[
    *router.urls,
    path(
        'passwordresetconfirm/<str:user_id>/<str:token>', 
        ResetPasswordConfirmViewSet.as_view({'post': 'post'}), 
        name='passwordresetconfirm'
    ),
]
