# from rest_framework.viewsets import ModelViewSet
from adrf.viewsets import ModelViewSet
from core_app_root.security.user.serializers.onboarding import OnboardingUserSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from core_app_root.security.user.models import OnboardingUserDetails
from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv()
class OnboardingUserViewset(ModelViewSet):
    permission_classes=[IsAuthenticated]
    http_method_names=['get','post']
    serializer_class=OnboardingUserSerializer
    queryset=OnboardingUserDetails.objects.all()
    async def create(self,request):
        serializer=self.serializer_class(data=request.data)
        try:

            if serializer.is_valid():

                # First, install the Twilio package with 'pip install twilio'

# Import the necessary libraries
                

                # Your Account SID and Auth Token from Twilio (make sure not to hard-code sensitive information)
                account_sid = os.environ["TWILIO_ACCOUNT_SID"]
                auth_token = os.environ["TWILIO_AUTH_TOKEN"]

                # Create a Twilio client
                client = Client(account_sid, auth_token)

                # Create a verification request
                verification = client.verify \
                    .v2 \
                    .services('VA504f70233378a0a1b19c7026765a7566') \
                    .verifications \
                    .create(to=f'{serializer.validated_data['phone']}', channel='sms')

                # Print the verification SID to confirm the request
                print(verification.sid)
                # serializer.user
                serializer.save()
                return Response({"status":True,"message":"Onboarding completed successfully ","data":serializer.data})
            else:
                return Response({"status":False,"message":"Onboarding did not complete due to invalid data,Try again later ","data":serializer.initial_data})
        except:
            return Response({"status":False,"message":"Internal server error, failed to complete ,Try again later ","data":serializer.initial_data})

    # def list(self,request):
    #     user_onboarding_list=OnboardingUserDetails.objects.all()
