from django.db import models

# Create your models here.
class AppleGiftingModel(models.Model):
    number_of_apples=models.IntegerField(blank=True,null=True)
    is_expired=models.BooleanField(default=False)