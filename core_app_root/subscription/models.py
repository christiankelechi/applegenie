from django.db import models

# Create your models here.
class Subscription(models.Model):
    click_subscription=models.BooleanField(default=False,null=True,blank=True)
    
    