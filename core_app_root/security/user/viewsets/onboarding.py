# from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ModelViewSet
from core_app_root.security.user.serializers.onboarding import OnboardingUserSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from core_app_root.security.user.models import OnboardingUserDetails
from twilio.rest import Client
from rest_framework import response
from rest_framework import status
from dotenv import load_dotenv
import os
load_dotenv()
class OnboardingUserViewset(ModelViewSet):
    permission_classes=[IsAuthenticated]
    http_method_names=['get','post']
    serializer_class=OnboardingUserSerializer
    queryset=OnboardingUserDetails.objects.all()
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        try:

            if serializer.is_valid():
                print("valid")
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
                # user=serializer.save()
                OnboardingUserDetails.objects.create(user=request.user, interests=serializer.validated_data['interests'],gender=serializer.validated_data['gender'],primary_interest=serializer.validated_data['primary_interest'],height=serializer.validated_data['height'],opening_move=serializer.validated_data['opening_move'],dob=serializer.validated_data['dob'],values=serializer.validated_data['values'],habits=serializer.validated_data['habits'],family_planning=serializer.validated_data['family_planning'],beliefs=serializer.validated_data['beliefs'],communities=serializer.validated_data['communities'],name=serializer.validated_data['name'],phone=serializer.validated_data['phone'],current_location=serializer.validated_data['current_location'],language=serializer.validated_data['language'],preference=serializer.validated_data['preference'],region=serializer.validated_data['region'])
                print("ok")
                return Response({"status":True,"message":"Onboarding completed successfully ","data":serializer.data},status=status.HTTP_200_OK)
            else:
                print("not valid in else block")
                return Response({"status":False,"message":"Onboarding did not complete due to invalid data,Try again later ","data":serializer.initial_data},status=status.HTTP_400_BAD_REQUEST)
        except:
            print("not valid")
            return Response({"status":False,"message":" could not create account ,Number already exist ","data":serializer.initial_data},status=status.HTTP_400_BAD_REQUEST)

    # def list(self,request):
    #     user_onboarding_list=OnboardingUserDetails.objects.all()
