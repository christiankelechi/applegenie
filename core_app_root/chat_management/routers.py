from rest_framework import routers
from core_app_root.chat_management.viewsets import chat_management
router=routers.SimpleRouter()
router.register(r'chat_management',chat_management.ChatManagementViewsets,basename='chat_management')
router.register(r'store_user_chats',chat_management.StoreUserChatViewSet,basename='store_user_chats')



urlpatterns=[
    *router.urls
]
