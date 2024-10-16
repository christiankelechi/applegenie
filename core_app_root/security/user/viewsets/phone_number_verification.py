# from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ModelViewSet
from core_app_root.security.user.serializers.phone_number_verification import PhoneNumberModelSerializer,OTPVerificationSerializer,ResendOtpSerializer

from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from core_app_root.security.user.models import PhoneNumbersModel
from twilio.rest import Client
from rest_framework import response
from rest_framework import status
from core_app_root.security.user.models import AppleModel
from dotenv import load_dotenv
import os
import random
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
load_dotenv()
import random

def generate_random_code():
    return random.randint(10000, 99999)



class PhoneNumberModelViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']
    serializer_class = PhoneNumberModelSerializer
    queryset = PhoneNumbersModel.objects.all()
    # parser_classes = [MultiPartParser, FormParser]  # Handles file uploads

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        try:
            if serializer.is_valid():
                # Twilio logic or other business logic
                account_sid = os.environ['TWILIO_ACCOUNT_SID']
                auth_token = os.environ['TWILIO_AUTH_TOKEN']
                message_service_sid=os.environ['MESSAGE_SERVICE_SID']
                code = generate_random_code()
                phone=str(serializer.validated_data['phone'])
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                    messaging_service_sid=message_service_sid,
                    body=f'Your OTP verification code for Finders Keepers app is {code}',
                    to=phone
                )
                print(message.sid)
                
                # Save the user
                # serializer.save(user=request.user, otp=str(code))
                PhoneNumbersModel.objects.update_or_create(
                     user=request.user,
                                 defaults={'code': code, 'phone': phone}
                          )
                # AppleModel.objects.create(user=request.user)
                
                # Return response with profile photo URL
                return Response({
                    "status": True,
                    "message": f"You will recieve otp soon ,check your device for  {request.user.email}",
                    "data": serializer.data,
                    
                }, status=status.HTTP_200_OK)

            else:
                return Response({
                    "status": False,
                    "message": "Could not process ,try again later",
                    "data": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print("Exception caught")
            # traceback.print_exc()  # Print the full traceback of the error
            return Response({
                "status": False, 
                "message": f"{str(e)}", 
                "data": serializer.initial_data
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class OtpVerficationViewset(ModelViewSet):
    permission_classes=[IsAuthenticated]
    
    serializer_class=OTPVerificationSerializer
    http_method_names=['post']
    
    # queryset=Otp.objects.all()
    # @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def create(self, request):
        serializer = self.serializer_class(data=request.data)  # Use the OTP serializer

        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            code = serializer.validated_data['code']

            try:
                onboarding_user = PhoneNumbersModel.objects.get(phone=phone, user=request.user)

                # Verify if the OTP matches
                if onboarding_user.code == code:
                    onboarding_user.code = None  # Clear the OTP after verification
                    onboarding_user.save()

                    return Response({"status": True, "message": "OTP verification successful."}, status=status.HTTP_200_OK)
                else:
                    return Response({"status": False, "message": "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)

            except PhoneNumbersModel.DoesNotExist:
                return Response({"status": False, "message": "User not found with this phone number."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"status": False, "message": "Invalid data.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

        
class ResendOtpViewset(ModelViewSet):
    permission_classes=[IsAuthenticated]
    
    serializer_class = ResendOtpSerializer
    queryset = PhoneNumbersModel.objects.all()
    http_method_names=['post']
    
    # queryset=Otp.objects.all()
    # @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        try:
            if serializer.is_valid():
                # Twilio logic or other business logic
                account_sid = os.environ['TWILIO_ACCOUNT_SID']
                auth_token = os.environ['TWILIO_AUTH_TOKEN']
                message_service_sid=os.environ['MESSAGE_SERVICE_SID']
                code = generate_random_code()
                phone=str(serializer.validated_data['phone'])
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                    messaging_service_sid=message_service_sid,
                    body=f'Your OTP verification code for Finders Keepers app is {code}',
                    to=phone)
                
                print(message.sid)
                
                # Save the user
                # serializer.save(user=request.user, otp=str(code))
                PhoneNumbersModel.objects.update_or_create(
                     user=request.user,
                                 defaults={'code': code, 'phone': phone}
                          )
                # AppleModel.objects.create(user=request.user)
                
                # Return response with profile photo URL
                return Response({
                    "status": True,
                    "message": f"You will recieve otp soon ,check your device for  {request.user.email}",
                    "data": serializer.data,
                    
                }, status=status.HTTP_200_OK)

            else:
                return Response({
                    "status": False,
                    "message": "Could not process ,try again later",
                    "data": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print("Exception caught")
            # traceback.print_exc()  # Print the full traceback of the error
            return Response({
                "status": False, 
                "message": f"{str(e)}", 
                "data": serializer.initial_data
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)