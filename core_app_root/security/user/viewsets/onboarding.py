# from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound
from rest_framework.viewsets import ModelViewSet
from core_app_root.security.user.serializers.onboarding import OnboardingUserSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from core_app_root.security.user.models import OnboardingUserDetails, User
from twilio.rest import Client
from rest_framework import response
from rest_framework import status
from core_app_root.security.user.models import AppleModel
from dotenv import load_dotenv
import os
from rest_framework.parsers import MultiPartParser, FormParser
import random
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
load_dotenv()
import random

def generate_random_code():
    return random.randint(10000, 99999)





import traceback  # To capture detailed exception info
from rest_framework import viewsets, filters
class OnboardingUserViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post','patch']
    serializer_class = OnboardingUserSerializer
    queryset = OnboardingUserDetails.objects.all()
   
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['user__email']  # Enable filtering by the user's email.
    search_fields = ['user__email']  # Enable searching by email.
    ordering_fields = ['user__email']  # Enable ordering/sorting by email.
    lookup_field = 'user__email'
    parser_classes=[MultiPartParser, FormParser]
     

    def get_queryset(self):
        return super().get_queryset().select_related('user')
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        try:
            if serializer.is_valid():
                # Twilio logic or other business logic
               
                # Save the user
                serializer.save(user=request.user)
                AppleModel.objects.create(user=request.user)
                
                # Return response with profile photo URL
                return Response({
                    "status": True,
                    "message": f"Onboarding completed successfully for {request.user.email}",
                    "data": serializer.data,
                    
                }, status=status.HTTP_200_OK)

            else:
                return Response({
                    "status": False,
                    "message": "Onboarding did not complete due to invalid data, try again later",
                    "data": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print("Exception caught")
            traceback.print_exc()  # Print the full traceback of the error
            return Response({
                "status": False, 
                "message": f"{str(e)}", 
                "data": serializer.initial_data
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # def get_object(self):
    #     # Retrieve the object using the user's email from URL kwargs.
    #     email = self.kwargs.get('email')
    #     try:
    #         # Get the related user by email and then retrieve the onboarding details.
    #         user = User.objects.get(email=email)
    #         obj = OnboardingUserDetails.objects.get(user=user)
    #         self.check_object_permissions(self.request, obj)
    #         return obj
    #     except User.DoesNotExist:
    #         raise NotFound(detail="User with this email does not exist.")
    #     except OnboardingUserDetails.DoesNotExist:
    #         raise NotFound(detail="Onboarding details for this user do not exist.")