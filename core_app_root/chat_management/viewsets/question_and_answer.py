from rest_framework import viewsets
from core_app_root.chat_management.serializers.question_and_answer import QuestionAndAnswerSerializer
from rest_framework.permissions import IsAuthenticated
from openai import OpenAI
import os
import openai
from rest_framework.response import Response
from core_app_root.security.user.models import User
from rest_framework import status
def applegeniesynopsis():
    
    response_output=" I am Ai Genie, your personal Companion, I will Help you to Seek truth and happiness so , so any question you need to know about your future life partner"
    return response_output
def apple_genie_ai_auto_reply(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-4o",
    max_tokens=1000,
    messages=[
        {"role": "system", "content": "You are a helpful companion."},
        {"role": "user", "content": str(prompt)}
    ]
    )

    response_output=completion.choices[0].message.content
    return response_output

class AiGenieSynopsisViewset(viewsets.ModelViewSet):
    http_method_names=['get']
    def list(self,request):
        synopsis=applegeniesynopsis()
        return Response({"status":True,"message":f" Hi {request.user}, {synopsis}"})
class QuestionAndAnswerViewsets(viewsets.ModelViewSet):
    serializer_class=QuestionAndAnswerSerializer
    http_method_names=['post','get']
    permission_classes=[IsAuthenticated]
    
   
   
        
    def create(self,request):
        try:
            serializer=self.serializer_class(data=request.data)
            if serializer.is_valid():
                
                prompt_response=apple_genie_ai_auto_reply(str(serializer.validated_data['prompt_in']))
                prompt_output=f"Hi {request.user} Welcome to Apple Genie Ai Personal Companion, your answer to your question are as follows : {prompt_response}"
                user=serializer.save()
                user.prompt_output=prompt_output
                user.save()
                return Response({"message":"Question answered successfully","prompt_response":prompt_output,"status":True,"data":serializer.validated_data},status=status.HTTP_200_OK)
            else:
                return Response({"message":"Invalid data provided","status":False,"data":serializer.validated_data},status=status.HTTP_406_NOT_ACCEPTABLE)
        except:
            return Response({"message":"Internal server error check your network and try again later","status":False,"data":serializer.validated_data},status=status.HTTP_406_NOT_ACCEPTABLE)
                
            