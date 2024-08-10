from rest_framework import viewsets
from core_app_root.match_friends.serializers.matched_frieds import MatchedFriendSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from core_app_root.match_friends.models import MatchedFriend
# This viewset performs the storage of matched users
class MatchedFriendViewset(viewsets.ModelViewSet):
    http_method_names=['post']
    serializer_class=MatchedFriendSerializer
    def create(self,request):
        try:
            serializer=self.serializer_class(data=request.data)
            
            if serializer.is_valid():
                user_email=serializer.validated_data['user_email']
                user_partner_email=serializer.validated_data['user_partner_email']
                serializer.save()
                
                return Response({"status":True,"message":"Matched successfully","users_matched":{"male":user_email,"female":user_partner_email}},status=status.HTTP_200_OK)
            else:
                return Response({"status":False,"message":"Invalid data sent","users_matched":None},status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response({"status":False,"message":"Internal Server error, try again later","users_matched":None},status=status.HTTP_500_INTERNAL_SERVER_ERROR)  
    
class MatchedFriendView(APIView):
    def get(self, request, *args, **kwargs):
        users_matched_list={"users_matched":{"user_emails":[ user.user_email for user in MatchedFriend.objects.all()]},"user_partner_emails":[ user_partner.user_partner_email for user_partner in MatchedFriend.objects.all()]}
        
        return Response({"status":True,"message":f" {users_matched_list}"},status=status.HTTP_200_OK)