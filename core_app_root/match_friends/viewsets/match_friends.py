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

import json
import os
import torch
from sentence_transformers import SentenceTransformer

from core_app_root.security.user.models import OnboardingUserDetails

# Load the DistilBERT model fine-tuned for semantic textual similarity
model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')

# Load user fixtures from JSON file
# with open('scripts/newusers.json', 'r') as f:
    # user_data = json.load(f)
# total_onboarding=OnboardingUserDetails.objects.all()

# # Ensure the output directory exists
# output_dir = 'scripts/user_dataset'
# os.makedirs(output_dir, exist_ok=True)

# # Process each user profile
# for current_user in total_onboarding:
#     user_email = current_user.user.email
    
#     # Create a profile string based on user details
#     profile_description = (
#         f"Name: {current_user['fields']['name']}, "
#         f"Interests: {', '.join(current_user['fields']['interests'])}, "
#         f"Gender: {current_user['fields']['gender']}, "
#         f"Primary Interest: {current_user['fields']['primary_interest']}, "
#         f"Height: {current_user['fields']['height']}, "
#         f"Opening Move: {current_user['fields']['opening_move']}, "
#         f"DOB: {current_user['fields']['dob']}, "
#         f"Location: {current_user['fields']['current_location']}, "
#         f"Language: {current_user['fields']['language']}, "
#         f"Bio: {current_user['fields']['bio']}, "
#         f"Education: {current_user['fields']['education']}, "

#         f"Preference: {', '.join(current_user['fields']['preference'])}, "
#         f"Region: {current_user['fields']['region']}"
#     )

#     # Generate embedding for the user profile
#     embedding = model.encode([profile_description])

#     # Save the embedding to a .pth file
#     file_path = os.path.join(output_dir, f'user_{user_email}_embedding.pth')
#     torch.save(embedding, file_path)
#     print(f"Saved embedding for User ID {user_email} to {file_path}")

# # To read an embedding by user ID
# def load_user_embedding(user_id):
#     file_path = os.path.join(output_dir, f'user_{user_id}_embedding.pth')
#     if os.path.exists(file_path):
#         return torch.load(file_path)
#     else:
#         raise FileNotFoundError(f"No embedding file found for User ID {user_id}.")

# # Example of loading a user embedding
# try:
#     user_embedding = load_user_embedding(1)  # Replace 1 with the desired user ID
#     print(f"Loaded embedding for User ID 1: {user_embedding}")
# except FileNotFoundError as e:
#     print(e)


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
                
                user_email_questions=requests.post(url=f"{bu.main_url}/history/user/questions/",json={'email':user_email})
                
                user_email_genie_questions=requests.post(url=f"{bu.main_url}/history/genie/questions/",json={'email':user_email})
                user_email_response=requests.post(url=f"{bu.main_url}/history/user/response/",json={'email':user_email})
                user_email_genie_response=requests.post(url=f"{bu.main_url}/history/genie/response/",json={'email':user_email})
                
                user_partner_email=str(serializer.data['user_partner_email'])
                
                user_partner_email_questions=requests.post(url=f"{bu.main_url}/history/user/questions/",json={'email':user_partner_email})
                
                user_partner_email_genie_questions=requests.post(url=f"{bu.main_url}/history/genie/questions/",json={'email':user_partner_email})
                user_partner_email_response=requests.post(url=f"{bu.main_url}/history/user/response/",json={'email':user_partner_email})
                user_partner_email_genie_response=requests.post(url=f"{bu.main_url}/history/genie/response/",json={'email':user_partner_email})
                
            
                user_response=requests.post(url=f"{bu.main_url}/chat/questionandanswer/",json={"email":user_email,"prompt_in":f"straight to point summary of the user detals just just the user likeness and all that: {user_email_questions.json()["response_data"]["total_user_questions"]},with questions {user_email_genie_questions.json()["response_data"]["total_user_questions"]}, {user_email_response.json()["response_data"]["total_user_questions"]}"})
                
                user_partner_response=requests.post(url=f"{bu.main_url}/chat/questionandanswer/",json={"email":user_partner_email,"prompt_in":f"straight to point summary of the user detals just just the user likeness and all that : {user_partner_email_questions.json()["response_data"]["total_user_questions"]},{user_partner_email_genie_questions.json()["response_data"]["total_user_questions"]}, {user_partner_email_response.json()["response_data"]["total_user_questions"]} compose it well and uniquely like a human"})
                
                users_matching_response=requests.post(url=f"{bu.main_url}/chat/questionandanswer/",json={"email":"kc@gmail.com","prompt_in":f"from the two user summary ,just straight to the point the summaries are as follows just write compatible or not compatible as single return{user_response.json()['prompt_response']},{user_partner_response.json()['prompt_response']}"})
                
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