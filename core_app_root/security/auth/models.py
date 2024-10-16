from django.db import models

# Create your models here.
class GoogleSignInModel(models.Model):
    user_id=models.CharField(max_length=100000,null=True,blank=True)
    name=mdels.CharField(max_length=1000,null=True,blank=True)
    email=models.EmailField(unique=True,null=True,blank=True)
    
    def __str__(self):
        return f"{self.email} signed in via google authentication"