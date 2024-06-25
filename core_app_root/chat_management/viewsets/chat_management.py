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
    http_method_names=['post','get','patch','delete']
    queryset=StoreUserChatModel.objects.all()
    
    
    def create(self,request):
        try:
            serializer=self.serializer_class(data=request.data)
            if serializer.is_valid():
                suggestion_question=str(serializer.validated_data['suggestion_question'])
                user_response=str(serializer.validated_data['user_response'])
                
                
                StoreUserChatModel.objects.create(user=request.user,suggestion_question=suggestion_question,user_response=user_response)
                
                
                context={"status":True,"detail":f"User Details Stored Successfully for user {request.user}"}
                return Response(context,status=status.HTTP_201_CREATED)
            else:
                context={"status":False,"detail":"Invalid field values provided"}
                
                return Response(context,status=status.HTTP_400_BAD_REQUEST)
                
        except:
            context={"status":False,"detail":"Request could not be processed successfully ,please check your network and try again "}
            
            return Response(context,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                

class ChatManagementViewsets(viewsets.ViewSet):
    serializer_class = ChatManagement
    http_method_names = ['get']

    def list(self, request):
        chat_client_model = ChatClientModel()  # Create an instance of ChatClientModel
        list_of_messages = chat_client_model.get_list_of_questions()
        context={"status": True, "message": "List of prompts fetched successfully", "data": [item[1] for item in list_of_messages]}
        return Response(context, status=status.HTTP_200_OK)
    
    
    
