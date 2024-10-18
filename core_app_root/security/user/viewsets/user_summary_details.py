# from datetime import date
# from core_app_root.security.user.models import OnboardingUserDetails
# from rest_framework import viewsets
# from core_app_root.security.user.serializers.user_profile_summary import UserProfileSummarySerializer
# from core_app_root.security.user.models import UserProfileSummary
# import requests
# from rest_framework.exceptions import NotFound
# from core_app_root import base_url
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
# from core_app_root.security.user.models import User,OnboardingUserDetails,AppleModel

# class UserProfileSummaryViewset(viewsets.ModelViewSet):
#     http_method_names = ['get','post']
#     serializer_class = UserProfileSummarySerializer
#     permission_classes=[IsAuthenticated]
#     queryset=UserProfileSummary.objects.all()
#     def create(self):
#         serializer=self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             interested_in=serializer.validated_data['interested_in']
#             language=serializer.validated_data['language']
#             age=serializer.validated_data['age_range']
#             amount_of_apple_range=serializer.validated_data['amount_of_apple_range']
#             travel_mode_on=serializer.validated_data['travel_mode_on']
#             distance_range=serializer.validated_data['distance_range']
#             interests=serializer.validated_data['interests']
#             sort_by_interest = OnboardingUserDetails.objects.all().filter(primary_interest__icontains=interested_in)
#             sort_by_language=OnboardingUserDetails.objects.all().filter(language__icontains=language)

#             sort_by_age = OnboardingUserDetails.objects.all().filter(age__icontains=age)
#             sort_by_amount_of_apple=AppleModel.objects.all().filter(bucket_of_apple__icontains=language)

#             sort_by_travel_mode = OnboardingUserDetails.objects.all().filter(current_location__icontains=travel_mode_on)

#             sort_by_distance = OnboardingUserDetails.objects.all().filter(current_location__icontains=distance_range)

#             sort_by_interests=OnboardingUserDetails.objects.all().filter(interests__icontains=interests)

            
#             sort_by_language=OnboardingUserDetails.objects.all().filter(language__icontains=language)
#             return Response({"status":True,"message":"User Created"},status=status.HTTP_200_OK)
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from core_app_root.security.user.models import OnboardingUserDetails, UserProfileSummary,AppleModel,User
from core_app_root.security.user.serializers.user_profile_summary import UserProfileSummarySerializer
from rest_framework.response import Response

class UserProfileSummaryViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = UserProfileSummarySerializer
    permission_classes = [IsAuthenticated]
    queryset = UserProfileSummary.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            interested_in = serializer.validated_data['interested_in']
            language = serializer.validated_data['language']
            age_range = serializer.validated_data['age_range']  # Expected as "min_age-max_age"
            amount_of_apple_range = serializer.validated_data['amount_of_apple_range']
            travel_mode_on = serializer.validated_data['travel_mode_on']
            distance_range = serializer.validated_data['distance_range']
            interests = serializer.validated_data['interests']

            # Extract minimum and maximum age
            try:
                min_age, max_age = map(int, age_range.split('-'))
            except ValueError:
                return Response({"status": False, "message": "Invalid age range format. Use 'min_age-max_age'."},
                                status=status.HTTP_400_BAD_REQUEST)

            # Filter users by different criteria
            users = OnboardingUserDetails.objects.filter(
                current_age__gte=min_age,
                current_age__lte=max_age,
                gender__icontains=interested_in,
                language__icontains=language,
                interests__icontains=interests,
                current_location__icontains=travel_mode_on,
              
            )

            # Filter users by amount_of_apple_range from AppleModel (e.g., "min_apple-max_apple")
            try:
                min_apple, max_apple = map(float, amount_of_apple_range.split('-'))
                apple_users = AppleModel.objects.filter(
                    user__in=users.values_list('user', flat=True),
                    bucket_of_apple__gte=min_apple,
                    bucket_of_apple__lte=max_apple
                ).values_list('user', flat=True)
            except ValueError:
                return Response({"status": False, "message": "Invalid apple range format. Use 'min_apple-max_apple'."},
                                status=status.HTTP_400_BAD_REQUEST)

            # Filter users based on those who match the apple criteria
            final_users = User.objects.filter(id__in=apple_users)

            # Serialize the final list of users
            user_data = UserProfileSummarySerializer(final_users, many=True).data

            return Response({"status": True, "message": "Filtered users retrieved successfully.", "data": user_data},
                            status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
