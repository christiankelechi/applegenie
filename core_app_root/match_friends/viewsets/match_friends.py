from rest_framework import viewsets
from core_app_root.match_friends.serializers import match_friends
from rest_framework import status
from rest_framework.response import Response
from core_app_root.match_friends.viewsets.fetchinterests import fetch_human_interests
import os
from core_app_root.human_attributes.models import HumanInterests
from core_app_root.human_attributes.serializers.human_attributes import HumanInterestSerializer
# class Interests(viewsets.ModelViewSet):

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
    
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            
            return Response({"status":True,},status=status.HTTP_200_OK)
        
    def list(self,request):
        
        return Response({"status":True},status=status.HTTP_200_OK)
        
        
        
        