from rest_framework import viewsets, status
from rest_framework.response import Response
from core_app_root.image_kyc.serializers.image_kyc_serializer import UserImageKycSerializer
from deepface import DeepFace
import io
from PIL import Image
import numpy as np
import os
class UserImageKycViewset(viewsets.ModelViewSet):
    serializer_class = UserImageKycSerializer
    http_method_names=['post']
    def create(self, request):
         try:
             serializer = self.serializer_class(data=request.data)

             if serializer.is_valid():
#                 # Save the serializer data (you might want to save it to the database)
                 # serializer.save()
                 response_data={}
                 # Get the image files from the serializer
                 user_default_image = serializer.validated_data['user_default_image']
                 user_real_time_capture = serializer.validated_data['user_real_time_capture']

#                 # Load images directly from the uploaded files
                 image1 = Image.open(user_default_image)
                 image2 = Image.open(user_real_time_capture)

#                 # Convert images to numpy arrays (DeepFace requires file paths or numpy arrays)
                 image1_array = np.array(image1)
                 image2_array = np.array(image2)
#                 # Perform image verification using DeepFace
                 result = DeepFace.verify(image1_array, image2_array)

                 if result['verified']==True:
#                 # Prepare the response data
                     response_data = {
                         'verified': result['verified'],
                         'status':True,
                         'message': "The images contain the same face." if result['verified'] else "The images do not contain the same face.",
                    
                     }
                 if result['verified']==False:
                 # Prepare the response data
                     response_data = {
                         'verified': result['verified'],
                         'status':False,
                         'message': "The images contain the same face." if result['verified'] else "The images do not contain the same face.",
                    
                     }

                
               
                
                 return Response(response_data, status=status.HTTP_200_OK)

             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

         except Exception as e:
             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

