# import os
# import uuid
# import cv2
# import torch
# import numpy as np
# from facenet_pytorch import MTCNN, InceptionResnetV1
# from rest_framework import status, viewsets
# from rest_framework.response import Response
# from core_app_root.image_kyc.serializers.image_kyc_serializer import UserImageKycSerializer

# class UserImageKycViewset(viewsets.ModelViewSet):
#     serializer_class = UserImageKycSerializer
#     http_method_names = ['post']

#     # Initialize MTCNN (face detector) and InceptionResnetV1 (FaceNet model)
#     mtcnn = MTCNN(image_size=160, margin=0, keep_all=True)
#     model = InceptionResnetV1(pretrained='vggface2').eval()

#     def preprocess_image(self, img_array):
#         # Convert the image array to RGB if needed (OpenCV loads images in BGR by default)
#         img_rgb = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
        
#         # Detect and crop faces from the image
#         img_cropped_list = self.mtcnn(img_rgb)
        
#         if img_cropped_list is not None and len(img_cropped_list) > 0:
#             img_embedding = self.model(img_cropped_list[0].unsqueeze(0))  # Get the face embedding
#             return img_embedding
#         else:
#             return None

#     def create(self, request):
#         try:
#             serializer = self.serializer_class(data=request.data)

#             if serializer.is_valid():
#                 response_data = {}

#                 # Get the image files from the serializer
#                 user_default_image = serializer.validated_data['user_default_image']
#                 user_real_time_capture = serializer.validated_data['user_real_time_capture']

#                 # Use in-memory file storage with Django's default File storage
#                 image1_temp = user_default_image.read()
#                 image2_temp = user_real_time_capture.read()

#                 # Convert image bytes to numpy arrays
#                 image1_array = cv2.imdecode(np.frombuffer(image1_temp, np.uint8), cv2.IMREAD_COLOR)
#                 image2_array = cv2.imdecode(np.frombuffer(image2_temp, np.uint8), cv2.IMREAD_COLOR)

#                 # Process the images
#                 embedding1 = self.preprocess_image(image1_array)
#                 embedding2 = self.preprocess_image(image2_array)

#                 # Compare the embeddings using Euclidean distance
#                 if embedding1 is not None and embedding2 is not None:
#                     distance = torch.dist(embedding1, embedding2).item()
#                     print(f"Distance between the two images: {distance}")

#                     # Define a threshold for recognition (e.g., 1.0 for FaceNet)
#                     threshold = 1.0
#                     if distance < threshold:
#                         response_data = {
#                             'verified': True,
#                             'status': True,
#                             'message': "The images contain the same face and can be verified"
#                         }
#                     else:
#                         response_data = {
#                             'verified': False,
#                             'status': False,
#                             'message': "The two faces are not similar",
#                         }
#                 else:
#                     response_data = {
#                         'verified': False,
#                         'status': False,
#                         'message': "No human face detected in the images",
#                     }

#                 return Response(response_data, status=status.HTTP_200_OK)

#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
import os
import uuid
import dlib
import cv2
import numpy as np
from rest_framework import status, viewsets
from rest_framework.response import Response
from core_app_root.image_kyc.serializers.image_kyc_serializer import UserImageKycSerializer

class UserImageKycViewset(viewsets.ModelViewSet):
    serializer_class = UserImageKycSerializer
    http_method_names = ['post']

    # Initialize dlib face detector and face recognition model
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('ai_libraries/dlib/shape_predictor_68_face_landmarks.dat')
    face_recognition_model = dlib.face_recognition_model_v1('ai_libraries/dlib/dlib_face_recognition_resnet_model_v1.dat')
    

    def preprocess_image(self, img_array):
        # Convert the image array to RGB if needed (OpenCV loads images in BGR by default)
        img_rgb = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
        
        # Optionally resize the image for better detection
        
        
        # Detect faces in the image
        detections = self.detector(img_rgb)
        if len(detections) == 0:
            return None

        # Process the first detected face
        face = detections[0]
        shape = self.predictor(img_rgb, face)
        face_descriptor = self.face_recognition_model.compute_face_descriptor(img_rgb, shape)
        
        return np.array(face_descriptor)

    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid():
                response_data = {}

                # Get the image files from the serializer
                user_default_image = serializer.validated_data['user_default_image']
                user_real_time_capture = serializer.validated_data['user_real_time_capture']

                # Use in-memory file storage with Django's default File storage
                image1_temp = user_default_image.read()
                image2_temp = user_real_time_capture.read()

                # Convert image bytes to numpy arrays
                image1_array = cv2.imdecode(np.frombuffer(image1_temp, np.uint8), cv2.IMREAD_COLOR)
                image2_array = cv2.imdecode(np.frombuffer(image2_temp, np.uint8), cv2.IMREAD_COLOR)

                # Process the images
                embedding1 = self.preprocess_image(image1_array)
                embedding2 = self.preprocess_image(image2_array)

                # Compare the embeddings using Euclidean distance
                if embedding1 is not None and embedding2 is not None:
                    distance = np.linalg.norm(embedding1 - embedding2)
                    print(f"Distance between the two images: {distance}")

                    # Define a threshold for recognition (e.g., 0.4 for dlib)
                    threshold = 0.4
                    if distance < threshold:
                        response_data = {
                            'verified': True,
                            'status': True,
                            'message': "The images contain the same face and can be verified"
                        }
                    else:
                        response_data = {
                            'verified': False,
                            'status': False,
                            'message': "The two faces are not similar",
                        }
                else:
                    response_data = {
                        'verified': False,
                        'status': False,
                        'message': "No human face detected in the images",
                    }

                return Response(response_data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
