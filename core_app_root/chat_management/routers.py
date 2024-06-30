from rest_framework import routers
from core_app_root.chat_management.viewsets import chat_management
from core_app_root.chat_management.viewsets import question_and_answer

router=routers.SimpleRouter()
router.register(r'chat/chat_management',chat_management.ChatManagementViewsets,basename='chat_management')
router.register(r'chat/store_user_chats',chat_management.StoreUserChatViewSet,basename='store_user_chats')
router.register(r'chat/questionandanswer',question_and_answer.QuestionAndAnswerViewsets,basename='questionandanswer')
router.register(r'chat/aigeniesynopsis',question_and_answer.AiGenieSynopsisViewset,basename='aigeniesynopsis')



urlpatterns=[
    *router.urls
]
