from django.urls import path
from core_app_root.match_friends.viewsets.matched_friend import MatchedFriendView
urlpatterns = [
    
path('match_friends/users/match/',MatchedFriendView.as_view(),name='match_users_match')
  
]