from django.db import models

# Create your models here.
from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='photos')
    tags = models.ManyToManyField('Tag', related_name='photos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)