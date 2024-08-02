from rest_framework import routers
from core_app_root.match_friends.viewsets import match_friends
router=routers.SimpleRouter()
router.register(r'match_friends',match_friends.MatchFriendsViewsets,basename='match_friend')


urlpatterns=[
    *router.urls
]

