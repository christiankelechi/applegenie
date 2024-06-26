from core_app_root.chat_management.serializers.chat_management import ChatManagement
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response 
from core_app_root.chat_management.models import ChatClientModel
from core_app_root.chat_management.serializers.chat_management import StoreUserChatSerializer
from core_app_root.chat_management.models import StoreUserChatModel
from rest_framework.permissions import AllowAny,IsAuthenticated
from core_app_root.chat_management.aimodels_scripts.user_synopsis import process_user_response
    
class StoreUserChatViewSet(viewsets.ModelViewSet):
    serializer_class=StoreUserChatSerializer
    permission_classes=[IsAuthenticated]
    http_method_names=['post','delete']
    queryset=StoreUserChatModel.objects.all()
    
    
    

class ChatManagementViewsets(viewsets.ViewSet):
    serializer_class = ChatManagement
    http_method_names = ['get']

    def list(self, request):
        chat_client_model = ChatClientModel()  # Create an instance of ChatClientModel
        list_of_messages = chat_client_model.get_list_of_questions()
        context={"status": True, "message": "List of prompts fetched successfully", "data": [item[1] for item in list_of_messages]}
        return Response(context, status=status.HTTP_200_OK)
    
    
    
    
