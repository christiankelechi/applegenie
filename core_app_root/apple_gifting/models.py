from django.db import models
from core_app_root.security.user.models import User
# Create your models here.
class AppleGiftingModel(models.Model):
    number_of_apples=models.IntegerField(blank=True,null=True)
    sender=models.ManyToManyField(User,on_delete=models.CASCADE)
    reciever=models.ManyToManyField(User,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.sender} sent total of {self.number_of_apples} to {self.reciever}"

class AppleModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rotting_apples=models.FloatField(default=0,null=True)
    accepted_apple=models.FloatField(default=0,null=True)
    is_expired=models.BooleanField(default=False,null=True)
    bucket_of_apple=models.FloatField(default=100,null=True)



    