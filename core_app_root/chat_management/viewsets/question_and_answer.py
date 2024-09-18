from rest_framework import viewsets
from core_app_root.chat_management.serializers.question_and_answer import QuestionAndAnswerSerializer
from rest_framework.permissions import IsAuthenticated
from openai import OpenAI
import os
from rest_framework.permissions import AllowAny
import openai
import asyncio
from rest_framework.response import Response
from core_app_root.security.user.models import User
from rest_framework import status
import re
import asyncio
from core_app_root.chat_management.viewsets.questionandanswer import chatRequest
import requests
from core_app_root import base_url
from core_app_root.chat_management.models import StoreUserChatModel,GenieResponseToUser,UserResponseToGenie,GenieQuestions,UserQuestions
from rest_framework.views import APIView
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import json
def applegeniesynopsis():
    
    response_output=" I am Ai Genie, your personal Companion, I will Help you to Seek truth and happiness so , so any question you need to know about your future life partner"
    return response_output
# async def apple_genie_ai_auto_reply(prompt):
#     openai.api_key = os.getenv("OPENAI_API_KEY")
#     client = OpenAI()

#     completion = client.chat.completions.create(
#     model="gpt-4o",
#     max_tokens=110,
#     messages=[
#         {"role": "system", "content": "You are a helpful companion."},
#         {"role": "user", "content": str(prompt)}
#     ]
#     )

#     response_output=completion.choices[0].message.content
#     return response_output
def remove_special_symbols(text):
    # Define a regular expression pattern to match non-alphanumeric characters
    pattern = r'[^a-zA-Z0-9\s]'
    # Use the sub() method to replace all non-alphanumeric characters with an empty string
    return re.sub(pattern, '', text)

class AiGenieSynopsisViewset(APIView):
    def get(self, request, *args, **kwargs):
        try:
            prompt_in=str(["What activities do you enjoy in your free time?","Do you have any favorite books, movies, or TV shows?","What are you looking for in a relationship?","Describe your ideal partner.","How do you typically spend your weekends?","What values are most important to you in a partner?",
    "Do you enjoy traveling? If so, what's your favorite destination?",
    "Are you more of a beach person or a mountain person?",
    "Do you prefer nights out or cozy evenings at home?",
    "What's your favorite type of cuisine?",
    "Tell us a bit about your background and upbringing.",
    "Are there any cultural traditions that are important to you?",
    "Where do you see yourself in the next five years?",
    "What are some goals you are currently working towards?",
    "If you could have dinner with any historical figure, who would it be and why?",
    "What's a fun fact about you that most people don't know?",
    "What type of apple best describes your personality and why?",
    "If you could gift an apple to anyone in history, who would it be and why?"])+str("using the above as dataset randomly ask question from it and also return a single question at a time  randomly concerning dating and all life question relating to dating ,love and personal relationship")
            email="dev.applematch@gmail.com"
            response=requests.post(url=f"{base_url.main_url}/chat/questionandanswer/",json={"email":"leoriza@gmail.com","prompt_in":prompt_in})
                    
            return Response({"status":True,"message":f" {response.json()['prompt_response']}"},status=status.HTTP_200_OK)

        except:
            return Response({"status":False,"message":f"Internal server error, check your network and try again"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class QuestionAndAnswerViewsets(viewsets.ModelViewSet):
    serializer_class = QuestionAndAnswerSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]

    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                
              
                prompt_output = str(chatRequest(str(serializer.data['prompt_in'])))
                return Response({"message": "Question answered successfully", "prompt_response": prompt_output, "status": True, "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid data provided", "status": False, "data": serializer.data}, status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            
            return Response({"message": "Internal server error check your network and try again later", "status": False, "data": serializer.data}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class QuestionAndAnswerViewsetsMain(viewsets.ModelViewSet):
    serializer_class = QuestionAndAnswerSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]

    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():

                prompt_in=str(serializer.data['prompt_in'])
                email=str(serializer.data['email'])
                response=requests.post(url=f"{base_url.main_url}/chat/questionandanswer/",json={"email":email,"prompt_in":prompt_in})
                
                UserQuestions.objects.create(email=email,user_questions=prompt_in)
                GenieResponseToUser.objects.create(email=email,genie_response=str(response.json()['prompt_response']))
                return Response({"message": "Response generated successfully", "status": True, "data": response.json()}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid data provided", "status": False, "data": serializer.data}, status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            
            return Response({"message": "Internal server error check your network and try again later", "status": False, "data": serializer.data}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class QuestionAndAnswerChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        prompt_in = text_data_json["prompt_in"]
        email = text_data_json["email"]
        # prompt_output=text_data["prompt_output"]

        # Call external API and save data asynchronously
        response = await self.get_api_response(prompt_in, email)

        # Send response back to WebSocket
        await self.send(text_data=json.dumps({
            "prompt_in": response.get("prompt_response"),
            "status": response.get("status"),
            "email": email
        }))

    async def get_api_response(self, prompt_in, email):
        try:
            api_url = f"{base_url.main_url}/chat/questionandanswer/"
            payload = {"email": email, "prompt_in": prompt_in}

            # Make the HTTP request asynchronously
            response = await sync_to_async(requests.post)(url=api_url, json=payload)

            # Process the response
            if response.status_code == 200:
                prompt_response = response.json().get('prompt_response')
                # Save user questions and responses asynchronously
                await self.save_user_data(email, prompt_in, prompt_response)
                return {"prompt_response": prompt_response, "status": True}
            else:
                return {"prompt_response": "Error in API call", "status": False}

        except Exception as e:
            return {"prompt_response": str(e), "status": False}

    @sync_to_async
    def save_user_data(self, email, prompt_in, prompt_response):
        UserQuestions.objects.create(email=email, user_questions=prompt_in)
        GenieResponseToUser.objects.create(email=email, genie_response=str(prompt_response))