from rest_framework import routers
from core_app_root.match_friends.viewsets import match_friends,matched_friend
router=routers.SimpleRouter()
router.register(r'match_friends/analyze',match_friends.MatchFriendsViewsets,basename='match_friend_analyze')
router.register(r'match_friends/match',matched_friend.MatchedFriendViewset,basename='matched_friend_match')



urlpatterns=[
    *router.urls
]

