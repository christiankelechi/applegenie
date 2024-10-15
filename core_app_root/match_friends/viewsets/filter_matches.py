from core_app_root.match_friends.serializers.filter_matches import FilterMatchesSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from core_app_root.security.user.models import OnboardingUserDetails
from core_app_root.security.user.models import AppleModel

class FilterMatchesVieset(viewsets.ModelViewSet):
    serializer_class=FilterMatchesSerializer
    http_method_names=['post']
    permission_classes=[IsAuthenticated]

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        interested_in=serializer.validaded_data['interested_in']
        if serializer.is_valid():
            primary_interest_details=OnboardingUserDetails.objects.all().filter(primary_interest__icontains=str(interested_in))
            age_range=OnboardingUserDetails.objects.all().filter()
            # filtered_users=
            return Response({"status":True,"message":"","data":serializer.data})