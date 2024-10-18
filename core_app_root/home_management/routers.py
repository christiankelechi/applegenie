from rest_framework import routers
from core_app_root.home_management.viewsets.home_management import HomeManagmentViewset
router=routers.SimpleRouter()
router.register(r'available-match-recommendation',HomeManagmentViewset,basename='home_management')


urlpatterns=[
    *router.urls
]
