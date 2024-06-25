from rest_framework import routers
from core_app_root.human_attributes.viewsets import human_attributes
router=routers.SimpleRouter()
router.register(r'human_attribute',human_attributes.HumanAttributesViewset,basename='human_attribute')


urlpatterns=[
    *router.urls
]
