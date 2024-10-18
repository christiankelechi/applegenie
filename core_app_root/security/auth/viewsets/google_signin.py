from rest_framework import viewsets
from core_app_root.security.auth.serializer.google_signin import GoogleSignInSerializer,GoogleLoginSerializer
from core_app_root.security.auth.models import GoogleSignInModel,GoogleLoginModel
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

class GoogleSignInViewSet(viewsets.ModelViewSet):
    serializer_class=GoogleSignInSerializer
    http_method_names=['post','get']
    permission_classes=[AllowAny]
    queryset=GoogleSignInModel.objects.all()

    def create(self,request):
        try:
            serializer=self.serializer_class(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({"status":True,"message":"Successfully signed up via google authentication","data":serializer.data})
        except Exception as e:
            return Response({"status":False,"message":f"{e}","data":serializer.data})

class GoogleLoginViewSet(viewsets.ModelViewSet):
    serializer_class = GoogleLoginSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]
    queryset=GoogleLoginModel.objects.all()

    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                # Find the user in the database using the email from the validated data
                email = serializer.validated_data.get('email')
                user = GoogleSignInModel.objects.get(email=email)

                
                    # Generate a new access token for the user
                refresh = RefreshToken.for_user(user)
                
                return Response({
                    "status": True,
                    "message": "Successfully logged in via Google authentication",
                    "refresh": str(refresh),
                    "access_token": str(refresh.access_token)
                }, status=status.HTTP_200_OK)
            
            return Response({
                "status": False,
                "message": "Invalid data",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "status": False,
                "message": f"Error: {e}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class GoogleLoginViewSet(viewsets.ModelViewSet):
#     serializer_class=GoogleLoginSerializer
#     http_method_names=['post']
#     permission_classes=[AllowAny]
#     queryset=GoogleSignInModel.objects.all()


#     def create(self,request):
#         try:
#             serializer=self.serializer_class(data=request.data)

#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({"status":True,"message":"Successfully signed up via google authentication","data":serializer.data})
#         except Exception as e:
#             return Response({"status":False,"message":f"{e}","data":serializer.data})