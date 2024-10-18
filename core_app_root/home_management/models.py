from django.db import models
from core_app_root.security.user.models import User
# Create your models here.
class HomeManagementView(models.Model):
    total_apples=models.TextField(null=True,blank=True)
    name=models.TextField(null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    apple_balance=models.TextField(null=True,blank=True)
    user_location=models.TextField(null=True,blank=True)
    current_user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    profile_image_string=models.CharField(null=True,blank=True)
    

class BookMarking(models.Model):
    user_book_marked=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)

    
class HomeGiftApple(models.Model):
    gifter=models.ForeignKey(User,on_delete=models.CASCADE)
    amount_to_gift = models.IntegerField(
    )
    

