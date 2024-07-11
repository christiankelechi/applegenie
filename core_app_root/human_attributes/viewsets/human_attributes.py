from rest_framework import viewsets
from core_app_root.human_attributes.serializers import human_attributes
from rest_framework import status
from rest_framework.response import Response
from core_app_root.apple_gifting import models
from rest_framework.permissions import AllowAny
from core_app_root.chat_management.aimodels_scripts.user_synopsis import process_user_response
from core_app_root.chat_management.models import StoreUserChatModel
class HumanAttributesViewset(viewsets.ModelViewSet):
    http_method_names=['post']
    serializer_class=human_attributes.HumanAttributesSerializer
    queryset=models.AppleGiftingModel.objects.all()
    permission_classes=[AllowAny]
    
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            context={"message":"Human Attributes Stored for this User","status":True,"data":serializer.data}
            return Response(context,status=status.HTTP_200_OK)
        else:
            context={"message":"Human Attributes could not be Stored for this User","status":False,"data":""}
            
            return Response(context,status=status.HTTP_406_NOT_ACCEPTABLE)
    
    
    # def list(self,request):
    #     stored_user_activity=StoreUserChatModel.objects.all().filter(user=request.user)
        
    #     user_characters=[]
    #     for activities in stored_user_activity:
            
    #         list_of_attributes=process_user_response(activities.suggestion_question,activities.user_response)
    #         user_characters.append({str(activities.suggestion_question):str(activities.user_response)})
    #     user_characters=user_characters
    #     context={"message":f"Human attributes of the user {request.user} fetched successfully ","status":False,"data":user_characters}
        
    #     return Response(context,status=status.HTTP_200_OK)