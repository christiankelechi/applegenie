from django.db import models

# Create your models here.
class HumanQualities(models.Model):
    # skin_color_types=(("G":"Gray","W":"White","B":"Black"))
    skin_color=models.CharField(null=True,blank=True,max_length=500)
    # body_size = ((
    #     "S": "Small",
    #     "M": "Medium",
    #     "H": "Huge",
    # ))
    body_size = models.CharField(max_length=200)
    # list_of_hobbies=(("SING","Singing","DANCE""DANCING","COOK":"COOKING"))
    
    hobbies=models.CharField(max_length=100)
    
    is_hot_tempered=models.BooleanField(default=False)
    
    