# from rest_framework import viewsets
# from core_app_root.home_management.serializers.home_management import HomeManagementSerializer
# from rest_framework import status
# from rest_framework.response import Response
# from core_app_root.apple_gifting import models
# from rest_framework.permissions import AllowAny
# from core_app_root.chat_management.aimodels_scripts.user_synopsis import process_user_response
# from core_app_root.chat_management.models import StoreUserChatModel
# from core_app_root.home_management.models import HomeManamentView
# from rest_framework.permissions import IsAuthenticated

# class HomeManagmentViewset(viewsets.ModelViewSet):
#     http_method_names=['get','post']
#     serializer_class=HomeManagementSerializer
#     queryset=HomeManamentView.objects.all()
#     permission_classes=[IsAuthenticated]
    
#     def create(self,request):
#         matches=[]
#         context={}
#         try:
#             # total_apples','name','age','apple_balance','user_email'
#             serializer=self.serializer_class(data=request.data)
#             if serializer.is_valid():
#                 starting_number_range=int(serializer.validated_data['starting_number_range'])-1
#                 ending_number_range=int(serializer.validated_data['ending_number_range'])-1

#                 if len(queryset) <=(ending_number_range+1):
                
#                     for available_match_user in self.queryset[starting_number_range,ending_number_range]:
#                         matches.append({"total_apples":available_match_user.total_apples,"name":available_match_user.name,"age":available_match_user.age,"apple_balance":available_match_user.apple_balance,"profile_image_string":available_match_user.profile_image_string})
#                     return Response({"status":True,"available_matches":matches,"message":"User matches fetched succesfully"},status=status.HTTP_200_OK)       
#                 else:
#                     return Response({"status":False,"available_matches":matches,"message":"Matches not available for the range you specified"},status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({"status":False,"errors":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
    
    
#     # def list(self,request):
#     #     stored_user_activity=StoreUserChatModel.objects.all().filter(user=request.user)
        
#     #     user_characters=[]
#     #     for activities in stored_user_activity:
            
#     #         list_of_attributes=process_user_response(activities.suggestion_question,activities.user_response)
#     #         user_characters.append({str(activities.suggestion_question):str(activities.user_response)})
#     #     user_characters=user_characters
#     #     context={"message":f"Human attributes of the user {request.user} fetched successfully ","status":False,"data":user_characters}
        
#     #     return Response(context,status=status.HTTP_200_OK)
from rest_framework import viewsets
from core_app_root.home_management.serializers.home_management import HomeManagementSerializer
from rest_framework import status
from rest_framework.response import Response
from core_app_root.home_management.models import HomeManagementView
from rest_framework.permissions import IsAuthenticated

class HomeManagmentViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = HomeManagementSerializer
    queryset = HomeManagementView.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request):
        matches = []
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                starting_number_range = int(serializer.validated_data['starting_number_range']) - 1
                ending_number_range = int(serializer.validated_data['ending_number_range']) - 1

                if len(self.queryset) > 0:
                    for available_match_user in self.queryset[starting_number_range:ending_number_range + 1]:
                        matches.append({
                            "total_apples": available_match_user.total_apples,
                            "name": available_match_user.name,
                            "age": available_match_user.age,
                            "apple_balance": available_match_user.apple_balance,
                            "profile_image_string": available_match_user.profile_image_string,
                            "User location":available_match_user.user_location
                        })
                    return Response({"status": True, "available_matches": matches, "message": "User matches fetched successfully"}, status=status.HTTP_200_OK)
                else:
                    return Response({"status": False, "available_matches": matches, "message": "Matches not available for the range you specified"}, status=status.HTTP_200_OK)

            return Response({"status": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"status": False, "errors": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)