from rest_framework import viewsets
from core_app_root.human_attributes.serializers import human_attributes
from rest_framework import status
from rest_framework.response import Response
from core_app_root.apple_gifting import models
from rest_framework.permissions import AllowAny

class HumanAttributesViewset(viewsets.ModelViewSet):
    http_method_names=['get','post']
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
    
    