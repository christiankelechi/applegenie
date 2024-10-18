from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from core_app_root.security.user.models  import User
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
    

class FilterMatches(models.Model):
    
    interested_in=models.CharField(max_length=200,null=True,blank=True)
    language=models.CharField(max_length=300,null=True,blank=True)
    age_range=models.CharField(max_length=300,null=True,blank=True)
    amount_of_apples=models.CharField(max_length=300,null=True,blank=True)
    travel_mode=models.CharField(default=False,null=True,blank=True)
    distance_range=models.CharField(default=False,null=True,blank=True)
    interests= ArrayField(
      models.CharField(max_length=100000,blank=True)
    )

    def __str__(self):
        return "Filtering performed successfuly"


class AiSuggestions(models.CharField):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    compatibilty_trait=models.TextField()