from django.db import models

# Create your models here.
class ChatClientModel(models.Model):
    # TODO field for getting all chat options
    prompt_message=models.TextField()
    
    