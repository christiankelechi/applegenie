from rest_framework import viewsets
from core_app_root.match_friends.serializers import match_friends
from rest_framework import status
from rest_framework.response import Response
from core_app_root.match_friends.viewsets.fetchinterests import fetch_human_interests
import os
from core_app_root.human_attributes.models import HumanInterests
from core_app_root.human_attributes.serializers.human_attributes import HumanInterestSerializer
# class Interests(viewsets.ModelViewSet):
import asyncio
import requests
from core_app_root import base_url as bu
from rest_framework.permissions import AllowAny

class HumanInterestsViewsets(viewsets.ViewSet):
    serializer_class=HumanInterestSerializer

    def list(self,request):
        file_path = os.path.join(os.getcwd(),'core_app_root/match_friends/viewsets/interests.json')
        interests = fetch_human_interests(file_path)
        print(interests)
        return Response({"status":True,"message":"List of interests fetched successfully","data":interests})
    
    def create(self,request):
        
        serializer=self.serializer_class(data=request.data)
        if serializer_class.is_valid():
            file_path=os.path.join(os.getcwd(),'core_app_root/match_friends/viewsets/interests.json')
            interest=fetch_human_interests(file_path)
            
            if HumanInterests.objects.get(user=request.user).DoesNotExist:
                user_inerests=serializer.save()
                
            return Response({"status":True,"message":"User Interests successfuly "})
    

class MatchFriendsViewsets(viewsets.ModelViewSet):
    
    serializer_class=match_friends.MatchFriendsSerializers
    
    http_method_names=['post']
    permission_classes = [AllowAny]
    def create(self,request):
        try:
            serializer=self.serializer_class(data=request.data)
            if serializer.is_valid():
                
                user_email=str(serializer.data['user_email'])
                
                user_email_questions=requests.post(url=f"{bu.main_url}history/user/questions/",json={'email':user_email})
                
                user_email_genie_questions=requests.post(url=f"{bu.main_url}history/genie/questions/",json={'email':user_email})
                user_email_response=requests.post(url=f"{bu.main_url}history/user/response/",json={'email':user_email})
                user_email_genie_response=requests.post(url=f"{bu.main_url}history/genie/response/",json={'email':user_email})
                
                user_partner_email=str(serializer.data['user_partner_email'])
                
                user_partner_email_questions=requests.post(url=f"{bu.main_url}history/user/questions/",json={'email':user_partner_email})
                
                user_partner_email_genie_questions=requests.post(url=f"{bu.main_url}history/genie/questions/",json={'email':user_partner_email})
                user_partner_email_response=requests.post(url=f"{bu.main_url}history/user/response/",json={'email':user_partner_email})
                user_partner_email_genie_response=requests.post(url=f"{bu.main_url}history/genie/response/",json={'email':user_partner_email})
                
            
                user_response=requests.post(url=f"{bu.main_url}/chat/questionandanswer/",json={"email":user_email,"prompt_in":f"straight to point summary of the user: {user_email_questions.json()["response_data"]["total_user_questions"]},with questions {user_email_genie_questions.json()["response_data"]["total_user_questions"]}, {user_email_response.json()["response_data"]["total_user_questions"]}"})
                
                user_partner_response=requests.post(url=f"{bu.main_url}/chat/questionandanswer/",json={"email":user_partner_email,"prompt_in":f"straight to point summary of the user details are as follows questions : {user_partner_email_questions.json()["response_data"]["total_user_questions"]},{user_partner_email_genie_questions.json()["response_data"]["total_user_questions"]}, {user_partner_email_response.json()["response_data"]["total_user_questions"]} compose it well and uniquely like a human"})
                
                users_matching_response=requests.post(url=f"{bu.main_url}/chat/questionandanswer/",json={"email":"kc@gmail.com","prompt_in":f"straight to point checking of the compatibility of the two summary for dating ..just check and say both are compartible or not from the two user summary ,just straight to the point the summaries are as follows {user_response.json()['prompt_response']},{user_partner_response.json()['prompt_response']}"})
                
                return Response({"status":True,"message":"Match analysis performed successfully","user_summary":user_response.json()['prompt_response'],"user_partner_summary":user_partner_response.json()['prompt_response'],"matching_message":users_matching_response.json()['prompt_response']},status=status.HTTP_200_OK)
        except:
            return Response({"status":False,"message":"Matching analysis could not be performed","user_summary":None},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def list(self,request):
        
        return Response({"status":True},status=status.HTTP_200_OK)
        
        
class AskQuestionsToMatchViewsets(viewsets.ModelViewSet):
    http_method_names=['post','get'] 
    serializer_class=match_friends.AskQuestionsToMatchSerializer
    
    def create(self,request):
        serializer=self.serializer_class(data=request.data) 
        if serializer.is_valid():
            
            return Response({"status":True})     
# 