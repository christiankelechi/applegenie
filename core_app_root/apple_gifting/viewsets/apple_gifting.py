from rest_framework import viewsets
from core_app_root.apple_gifting.serializers import apple_gifting
from rest_framework import status
from rest_framework.response import Response
from core_app_root.security.user import models
from rest_framework.permissions import AllowAny,IsAuthenticated
from core_app_root.security.user.models import AppleModel,AppleGiftingModel
class AppleGiftingViewset(viewsets.ModelViewSet):
    http_method_names=['get','post']
    serializer_class=apple_gifting.AppleGiftingSerializer
    queryset=models.AppleGiftingModel.objects.all()
    permission_classes=[IsAuthenticated]

    queryset=AppleGiftingModel.objects.all()
    
    def create(self,request):
        try:
            context={}
            serializer=self.serializer_class(data=request.data)
            if serializer.is_valid():
                # print("valid")
                number_of_apples=serializer.validated_data['number_of_apples']
                sender=serializer.validated_data['sender']
                reciever=serializer.validated_data['reciever']
                # print(f"{sender} and {reciever}")
                reciever_accepts=serializer.validated_data['reciever_accepts']
                # print(reciever_accepts)
                check_amount_of_apple=AppleModel.objects.get(user__email=str(sender))
                # print(check_amount_of_apple.bucket_of_apple)
                # print(reciever_accepts)
                # try:
                #     check_amount_of_apple = AppleModel.objects.get(user=request.user)
                # except AppleModel.DoesNotExist:
                #     context = {"status": False, "message": "User does not have any apples"}
                #     return Response(context, status=status.HTTP_404_NOT_FOUND)
                # print(check_amount_of_apple)
                current_apple_amount=float(check_amount_of_apple.bucket_of_apple)
                if float(number_of_apples)>=float(current_apple_amount) :
                #     print(number_of_apples)
                        
                    context={"status":False,"message":f"{sender} could not send any apple out at the moment due to insufficient apple balance","data":serializer.data}
                    return Response(context,status=status.HTTP_403_FORBIDDEN)

                else:
                    # print("ok")
                    reciever_user=AppleModel.objects.get(user__email=reciever)
                    print(reciever_user)
                    reciever_user.save()
                    reciever_user.bucket_of_apple=float(number_of_apples)+float(reciever_user.bucket_of_apple)
                    reciever_user.save()
                    sender_user=AppleModel.objects.get(user__email=str(sender))

                    sender_user.bucket_of_apple=float(sender_user.bucket_of_apple)-float(number_of_apples)
                    sender_user.total_apple_sent=float(sender_user.total_apple_sent)+float(number_of_apples)
                    sender_user.save()
                    serializer.save()
                    context={"status":True,"message":f"{sender} sent across {number_of_apples} apples to {reciever}" }
                    return Response(context,status=status.HTTP_200_OK)
        
        except:
            context={"status":False,"message":f"could not complete this request, try again later" }
            return Response(context,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

