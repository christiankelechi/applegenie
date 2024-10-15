from datetime import date
from core_app_root.security.user.models import OnboardingUserDetails
from rest_framework import viewsets
from core_app_root.security.user.serializers.user_profile_summary import UserProfileSummarySerializer
from core_app_root.security.user.models import UserProfileSummary
import requests
from rest_framework.exceptions import NotFound
from core_app_root import base_url
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class UserProfileSummaryViewset(viewsets.ModelViewSet):
    http_method_names = ['get','post']
    serializer_class = UserProfileSummarySerializer
    permission_classes=[IsAuthenticated]
    user_profile_summary=UserProfileSummary.objects.all()
    def create(self):
        return Response({"status":True,"message":"User Created"},status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        # Retrieve by UUID
        try:
            user_auth_details=requests.get(f"{base_url.backend_url}/user/{request.user.id}")
            user_onboarding_details=request.get(f"{base_url.backend_url}/onboarding/{request.user__email}")
            return Response({"status":True,"data":{"auth_detais":user_auth_details,"onboading_details":user_onboarding_details}}, status=status.HTTP_200_OK)
        except UserProfileSummary.DoesNotExist:
            raise NotFound("User profile summary not found.")


# # Retrieve the user by email
# current_user = OnboardingUserDetails.objects.get(user__email="christiankelechieze@gmail.com")
# print(f"{current_user.user.email} has completed the onboarding stage.")

# # Directly use the dob from the retrieved user details
# dob = current_user.dob
# print(f"Date of birth: {dob}")

# # Current date in 2024
# current_date = date(2024, 10, 15)

# # Calculate the age using the fetched date of birth
# age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))

# print(f"The user's age in 2024 is: {age}")
