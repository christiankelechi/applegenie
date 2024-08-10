from core_app_root.chat_management.serializers.chat_management import ChatManagement
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response 
from core_app_root.chat_management.models import ChatClientModel
from core_app_root.chat_management.serializers.chat_management import StoreUserChatSerializer
from core_app_root.chat_management.models import StoreUserChatModel
from rest_framework.permissions import AllowAny,IsAuthenticated
from core_app_root.chat_management.aimodels_scripts.user_synopsis import process_user_response
from core_app_root.chat_management.serializers.chat_management import UserQuestionsHistorySerializer,UserResponseHistorySerializer,GenieQuestionsHistorySerializer,GenieResponseHistorySerializer
from core_app_root.chat_management.models import UserHistory
from core_app_root.chat_management.models import UserQuestions,UserResponseToGenie,GenieQuestions,GenieResponseToUser
# import logging
# logger=logging.getLogger(__name__)
# logging.basicConfig(filename='errorlog.log', encoding='utf-8', level=logging.DEBUG)

class StoreUserChatViewSet(viewsets.ModelViewSet):
    serializer_class=StoreUserChatSerializer
    permission_classes=[AllowAny]
    http_method_names=['post']
    def create(self,request):
        try:
            serializer=self.serializer_class(data=request.data)
            if serializer.is_valid():
                email=str(serializer.validated_data['email'])
                suggestion_question=str(serializer.validated_data['suggestion_question'])
                user_response=str(serializer.validated_data['user_response'])
        
                # StoreUserChatModel.objects.create(email=email,suggestion_question=suggestion_question,user_response=user_response)
                
                GenieQuestions.objects.create(email=email,genie_question=suggestion_question)
                UserResponseToGenie.objects.create(email=email,user_response=user_response)

                return Response({"status":True,"message":"User answered question asked by the Genie","response_data":{"data":serializer.validated_data}},status=status.HTTP_200_OK)   
            else:
                return Response({"status":True,"message":"Invalid data","response_data":{"data":serializer.data}},status=status.HTTP_400_BAD_REQUEST)   
        
        except:
            return Response({"status":False,"message":"Check Network and Try again later"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ChatManagementViewsets(viewsets.ViewSet):
    serializer_class = ChatManagement
    http_method_names = ['get']
    permission_classes=[AllowAny]
    
    def list(self, request):
        chat_client_model = ChatClientModel()  # Create an instance of ChatClientModel
        list_of_messages = chat_client_model.get_list_of_questions()
        context={"status": True, "message": "List of prompts fetched successfully", "data": [item[1] for item in list_of_messages]}
        return Response(context, status=status.HTTP_200_OK)
    
    
    

class QuestionAskByUser(viewsets.ModelViewSet):
    serializer_class=UserQuestionsHistorySerializer
    http_method_names = ['post']
    permission_classes=[AllowAny]
    def create(self,request):
       
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            email=str(serializer.validated_data['email'])
            questions_ask_by_user=UserQuestions.objects.filter(email__icontains=email)
            if len(questions_ask_by_user)<=30:
                
                user_questions = [history.user_questions for history in questions_ask_by_user]
                
            
                
                return Response({"status":True,"response_data":{"total_user_questions":user_questions}},status=status.HTTP_200_OK)   

            else:
                user_questions = [history.user_questions for history in questions_ask_by_user[-30:]]
                return Response({"status":True,"response_data":{"total_user_questions":user_questions}},status=status.HTTP_200_OK)   
                    
                
      
class QuestionAskByGenie(viewsets.ModelViewSet):
    serializer_class=GenieQuestionsHistorySerializer
    http_method_names = ['post']
    permission_classes=[AllowAny]
    def create(self,request):
       
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            email=str(serializer.validated_data['email'])
            questions_ask_by_genie=GenieQuestions.objects.filter(email__icontains=email)
            
            if len(questions_ask_by_genie)<=30:
                genie_questions = [history.genie_question for history in questions_ask_by_genie]
                
            
                
                return Response({"status":True,"response_data":{"total_user_questions":genie_questions}},status=status.HTTP_200_OK)   
            else:
                genie_questions = [history.genie_question for history in questions_ask_by_genie[-30:]]
                
            
                
                return Response({"status":True,"response_data":{"total_user_questions":genie_questions}},status=status.HTTP_200_OK)  
                

class QuestionAnsweredByUser(viewsets.ModelViewSet):
    serializer_class=UserResponseHistorySerializer
    http_method_names = ['post']
    permission_classes=[AllowAny]
    def create(self,request):
       
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            email=str(serializer.validated_data['email'])
            questions_answered_by_user=UserResponseToGenie.objects.filter(email__icontains=email)
            
            if len(questions_answered_by_user)<=30:
                user_questions_answered = [history.user_response for history in questions_answered_by_user]
                
            
                
                return Response({"status":True,"response_data":{"total_user_questions":user_questions_answered}},status=status.HTTP_200_OK)   
            else: 
                user_questions_answered = [history.user_response for history in questions_answered_by_user[-30:]]
                
            
                
                return Response({"status":True,"response_data":{"total_user_questions":user_questions_answered}},status=status.HTTP_200_OK)   
        
class QuestionAnsweredByGenie(viewsets.ModelViewSet):
    serializer_class=GenieResponseHistorySerializer
    http_method_names = ['post']
    permission_classes=[AllowAny]
    def create(self,request):
       
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            email=str(serializer.validated_data['email'])
            questions_answered_by_genie=GenieResponseToUser.objects.filter(email__icontains=email)
            
            if len(questions_answered_by_genie)<=30:
                genie_questions_answered = [history.genie_response for history in questions_answered_by_genie]
            
            
          
            
                return Response({"status":True,"response_data":{"total_user_questions":genie_questions_answered}},status=status.HTTP_200_OK)   
            else:
                genie_questions_answered = [history.genie_response for history in questions_answered_by_genie[-30:]]
            
            
          
            
                return Response({"status":True,"response_data":{"total_user_questions":genie_questions_answered}},status=status.HTTP_200_OK) 
                