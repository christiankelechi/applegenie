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
class AiGenieSynopsisViewset(viewsets.ModelViewSet):
    http_method_names=['get']
    def list(self,request):
        synopsis=applegeniesynopsis()
        return Response({"status":True,"message":f" Hi {request.user}, {synopsis}"})



class QuestionAndAnswerViewsets(viewsets.ModelViewSet):
    serializer_class = QuestionAndAnswerSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]

    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                
                openai.api_key = os.getenv("OPENAI_API_KEY")
                prompt_output = str(asyncio.run(chatRequest(str(serializer.data['prompt_in']))))
                return Response({"message": "Question answered successfully", "prompt_response": prompt_output, "status": True, "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid data provided", "status": False, "data": serializer.data}, status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            
            return Response({"message": "Internal server error check your network and try again later", "status": False, "data": serializer.data}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# class QuestionAndAnswerViewsets(viewsets.ModelViewSet):
#     serializer_class=QuestionAndAnswerSerializer
#     http_method_names=['post']
#     permission_classes=[AllowAny]
    
   
   
        
#     def create(self,request):
#     # try:
#         serializer=self.serializer_class(data=request.data)
#         # if serializer.is_valid():
        
#         openai.api_key = os.getenv("OPENAI_API_KEY")
#         client = OpenAI()

#         completion = client.chat.completions.create(
#         model="gpt-4o",
#         max_tokens=90,
#         messages=[
#             {"role": "system", "content": "You are a helpful companion."},
#             {"role": "user", "content": str(serializer.data['prompt_in'])}
#         ]
#         )
        
#         response_output=completion.choices[0].message.content
#         # prompt_response=asyncio.run(apple_genie_ai_auto_reply(str(serializer.validated_data['prompt_in'])))
#         prompt_output=remove_special_symbols(response_output)
    
#         # user.save()
        
#         return Response({"message":"Question answered successfully","prompt_response":prompt_output,"status":True,"data":serializer.data},status=status.HTTP_200_OK)
#         # else:
            
#         #     return Response({"message":"Invalid data provided","status":False,"data":serializer.validated_data},status=status.HTTP_406_NOT_ACCEPTABLE)
#     # except:
        
#     #     return Response({"message":"Internal server error check your network and try again later","status":False,"data":serializer.validated_data},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    