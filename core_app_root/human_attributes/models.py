from django.db import models
from core_app_root.security.user.models import User
# Create your models here.
class HumanQualities(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    age=models.IntegerField(default=18)
    
    country=models.CharField(max_length=10000,null=True,blank=True)

    

class HumanInterests(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    nature=models.BooleanField(default=False)
    travel=models.BooleanField(default=False)
    writing=models.BooleanField(default=False)
    people=models.BooleanField(default=False)
    gym_and_fitness=models.BooleanField(default=False)
    language=models.BooleanField(default=False)
    photography=models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural='HumanInterests'
    
    
    
    
    
    
    
    
    