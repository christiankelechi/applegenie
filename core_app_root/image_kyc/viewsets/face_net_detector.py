import torch
from facenet_pytorch import InceptionResnetV1, MTCNN
from PIL import Image
import numpy as np

# Initialize MTCNN (face detector) and InceptionResnetV1 (FaceNet model)
mtcnn = MTCNN(image_size=160, margin=0)
model = InceptionResnetV1(pretrained='vggface2').eval()

# Load and preprocess the images
def preprocess_image(image_path):
    img = Image.open(image_path)
    img_cropped = mtcnn(img)  # Detect and crop the face
    if img_cropped is not None:
        img_embedding = model(img_cropped.unsqueeze(0))  # Get the face embedding
        return img_embedding
    else:
        return None

embedding1 = preprocess_image('path/to/first/image.jpg')
embedding2 = preprocess_image('path/to/second/image.jpg')

# Compare the embeddings using Euclidean distance
if embedding1 is not None and embedding2 is not None:
    distance = torch.dist(embedding1, embedding2).item()
    print(f"Distance between the two images: {distance}")
    
    # Define a threshold for recognition (e.g., 1.0 for FaceNet)
    threshold = 1.0
    if distance < threshold:
        print("The faces are similar")
    else:
        print("The faces are not similar")
else:
    print("Face not detected in one or both images")
