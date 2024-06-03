from django.db import models

# Create your models here.
class AppleGiftingModel(models.Model):
    number_of_apples=models.IntegerField(db_default=0,null=True)
    is_expired=models.BooleanField(default=False)