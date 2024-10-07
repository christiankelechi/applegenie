from rest_framework.viewsets import ModelViewSet
from core_app_root.security.user.serializers.onboarding import OnboardingUserSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from core_app_root.security.user.models import OnboardingUserDetails
class OnboardingUserViewset(ModelViewSet):
    permission_classes=[AllowAny]
    http_method_names=['get','post']
    serializer_class=OnboardingUserSerializer
    queryset=OnboardingUserDetails.objects.all()
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        try:

            if serializer.is_valid():
                serializer.save()
                return Response({"status":True,"message":"Onboarding completed successfully ","data":serializer.data})
            else:
                return Response({"status":False,"message":"Onboarding did not complete due to invalid data,Try again later ","data":serializer.data})
        except:
            return Response({"status":False,"message":"Internal server error, failed to complete ,Try again later ","data":serializer.data})

    # def list(self,request):
