from django.db import models
from django.utils import timezone
# Create your models here.
class UserAttributes(models.Model):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_NOT_SPECIFIED = 'not specified'
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_NOT_SPECIFIED, 'Not specified')
    ]
    gender = models.CharField(max_length=1000, choices=GENDER_CHOICES,null=True,blank=True)
    
    age=models.IntegerField(default=18)
    
    country=models.CharField(max_length=10000,null=True,blank=True)
    
class AskQuestionsToMatchModel(models.Model):
    prompt_in=models.TextField()
    prompt_out=models.TextField()
    
    def __str__(self):
        return f" Answered your question  on {self.prompt_in}"
    

class MatchFriend(models.Model):
    user_email=models.TextField(null=True,blank=True)
    user_partner_email=models.TextField(null=True,blank=True)
    user_email_summary=models.TextField(null=True,blank=True)
    user_partner_email_summary=models.TextField(null=True,blank=True)

    
class MatchedFriend(models.Model):
    user_email=models.TextField(null=True,blank=True)
    user_partner_email=models.TextField(null=True,blank=True)
    swipe_right=models.BooleanField(null=True,blank=True,default=False)
    swipe_left=models.BooleanField(null=True,blank=True,default=False)
    time_matched=models.DateTimeField(auto_now=True)
    