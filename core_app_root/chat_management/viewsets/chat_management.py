from core_app_root.chat_management.serializers.chat_management import ChatManagement
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response 
from core_app_root.chat_management.models import ChatClientModel
from core_app_root.chat_management.serializers.chat_management import StoreUserChatSerializer
from core_app_root.chat_management.models import StoreUserChatModel
from rest_framework.permissions import AllowAny,IsAuthenticated

    
    # def create(self)
    
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
                
                
                user=serializer.save()
                
                
                context={"status":True,"detail":"User Details Stored Successfully"}
                return Response(context,status=status.HTTP_201_OK)
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
    
    
    
    