from core_app_root.security.auth.viewsets.password import ResetPasswordViewSet, ResetPasswordConfirmViewSet
from core_app_root.security.auth.viewsets.register import RegisterViewSet
from core_app_root.security.auth.viewsets.login import LoginViewSet
from rest_framework import routers
from django.urls import path
router=routers.SimpleRouter()
router.register(r'register',RegisterViewSet,basename='register')
router.register(r'login',LoginViewSet,basename='login')
router.register(r'passwordreset', ResetPasswordViewSet, basename="passwordreset")


urlpatterns=[
    *router.urls,
    path(
        'passwordresetconfirm/<str:user_id>/<str:token>', 
        ResetPasswordConfirmViewSet.as_view({'post': 'post'}), 
        name='passwordresetconfirm'
    ),
]
