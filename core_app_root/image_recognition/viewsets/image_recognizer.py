from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from core_app_root.image_recognition.models import Photo, Tag
from core_app_root.image_recognition.serializers.image_recognizer import PhotoSerializer
import cv2
import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import img_to_array
from rest_framework.permissions import IsAuthenticated,AllowAny
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    http_method_names=['post','get']
    permission_classes=[AllowAny]
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # Load the ResNet50 model
            model = ResNet50(weights='imagenet', include_top=True)

            # Preprocess the uploaded image
            img_file = request.FILES['image']
            img_array = cv2.imdecode(np.frombuffer(img_file.read(), np.uint8), cv2.IMREAD_COLOR)
            
            # Resize the image to 224x224
            img_resized = cv2.resize(img_array, (224, 224))
            
            img = img_to_array(img_resized)
            img = np.expand_dims(img, axis=0)
            img = preprocess_input(img)

            # Classify the image using ResNet50
            preds = model.predict(img)
            predicted_tags = [label[1] for label in decode_predictions(preds, top=5)[0]]

            # Create the Photo instance and save it
            photo = serializer.save()

            # Create Tag instances and associate them with the Photo
            for tag_name in predicted_tags:
                tag, _ = Tag.objects.get_or_create(name=tag_name, category='ResNet50')
                photo.tags.add(tag)

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
        except:
            return Response({"status":False,"message":"Check your network and try again"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
