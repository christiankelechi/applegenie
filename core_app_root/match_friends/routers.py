from rest_framework import routers
from core_app_root.match_friends.viewsets import match_friends,matched_friend,filter_matches
router=routers.SimpleRouter()
router.register(r'match_friends/analyze',match_friends.MatchFriendsViewsets,basename='match_friend_analyze')
router.register(r'match_friends/match',matched_friend.MatchedFriendViewset,basename='matched_friend_match')
router.register(r'match_friends/filter',filter_matches.FilterMatchesVieset,basename='matched_friend_filter')




urlpatterns=[
    *router.urls
]

