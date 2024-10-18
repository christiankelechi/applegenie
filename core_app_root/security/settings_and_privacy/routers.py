#!/usr/bin/env python3
from core_app_root.security.settings_and_privacy.viewset.setting import DisplaySettingViewSet
from rest_framework import routers


router=routers.SimpleRouter()
router.register(r'settings', DisplaySettingViewSet, basename="Setting Viewset")


urlpatterns=[
    *router.urls
]
