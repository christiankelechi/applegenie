from django.db import models

# Create your models here.
class HumanQualities(models.Model):
    skin_color_types={"G":"Gray","W":"White","B":"Black"}
    skin_color=models.CharField(null=True,blank=True,max_length=500,choices=skin_color_types)
    body_size = {
        "S": "Small",
        "M": "Medium",
        "H": "Huge",
    }
    shirt_size = models.CharField(max_length=1, choices=body_size)
    list_of_hobbies={"SING":"Singing","DANCE":"DANCING","COOK":"COOKING"}
    
    hobbies=models.CharField(max_length=100,choices=list_of_hobbies)
    
    is_hot_tempered=models.BooleanField(default=False)
    
    