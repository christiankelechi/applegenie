from django.urls import path
from core_app_root.chat_management.viewsets.question_and_answer import AiGenieSynopsisViewset
urlpatterns = [
    
path('chat/aigeniesynopsis',AiGenieSynopsisViewset.as_view(),name='aigeniesynopsis')
  
]