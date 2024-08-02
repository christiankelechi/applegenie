from rest_framework import routers
from core_app_root.chat_management.viewsets import chat_management
from core_app_root.chat_management.viewsets import question_and_answer

router=routers.SimpleRouter()
router.register(r'history/user/questions',chat_management.QuestionAskByUser,basename='user_questions')
router.register(r'history/genie/questions',chat_management.QuestionAskByGenie,basename='user_genie')
router.register(r'history/user/response',chat_management.QuestionAnsweredByUser,basename='response_user')
router.register(r'history/genie/response',chat_management.QuestionAnsweredByGenie,basename='response_genie')

router.register(r'chat/chat_management',chat_management.ChatManagementViewsets,basename='chat_management')
router.register(r'chat/store_user_chats',chat_management.StoreUserChatViewSet,basename='store_user_chats')
router.register(r'chat/questionandanswer',question_and_answer.QuestionAndAnswerViewsets,basename='questionandanswer')
router.register(r'chat/questionandanswer_main',question_and_answer.QuestionAndAnswerViewsetsMain,basename='questionandanswer_main')





urlpatterns=[
    *router.urls
]
