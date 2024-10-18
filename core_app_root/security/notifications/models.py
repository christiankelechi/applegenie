from django.db import models

# Create your models here.
class UserProfileNotifications(models.Model):
    date_intervals=models.DateField(null=True,blank=True)
    profile_image_string=models.CharField(null=True,blank=True)
    apple_message_alert=models.TextField(null=True,blank=True)
    amount_sent=models.TextField(null=True,blank=True)
    days_remaining_to_accept=models.CharField(null=True,blank=True)