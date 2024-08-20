from rest_framework import viewsets
from core_app_root.apple_gifting.serializers import apple_gifting
from rest_framework import status
from rest_framework.response import Response
from core_app_root.apple_gifting import models
from rest_framework.permissions import AllowAny

class AppleGiftingViewset(viewsets.ModelViewSet):
    http_method_names=['get','post']
    serializer_class=apple_gifting.AppleGiftingSerializer
    queryset=models.AppleGiftingModel.objects.all()
    permission_classes=[AllowAny]
    def create(self,request):
        context={"message":"Gift an apple"}
        return Response(context,status=status.HTTP_200_OK)
    
    