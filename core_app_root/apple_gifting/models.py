from django.db import models
from core_app_root.security.user.models import User
# Create your models here.
class AppleGiftingModel(models.Model):
    number_of_apples=models.IntegerField(blank=True,null=True)
    sender=models.EmailField(blank=True,null=True)

    reciever=models.EmailField(blank=True,null=True)
    reciever_accepts=models.BooleanField(default=False,null=True,blank=True)
    reciever_rejects=models.BooleanField(default=False,null=True,blank=True)


    def __str__(self):
        return f"{self.sender} sent total of {self.number_of_apples} apples to {self.reciever}"

class AppleModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    rotting_apples=models.FloatField(default=0,null=True)
    apple_recieved=models.FloatField(default=0,null=True)
    total_apple_sent=models.FloatField(default=0,null=True)
    accepted_apple=models.FloatField(default=0,null=True)
    is_expired=models.BooleanField(default=False,null=True)
    bucket_of_apple=models.FloatField(default=10,null=True)


    def __str__(self):
        return f"{self.user} Apple Profile Details"