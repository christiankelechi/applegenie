#!/usr/bin/env python3
from core_app_root.security.user.models import User
from multiselectfield import MultiSelectField
from django.db import models
from typing import Dict
import uuid

habit_choices = [
    ['Y', "Yes"], ['S', "Sometimes"], ['N', "No"]
]
education_choices = (
    ("Technical Eduation", "Technical Education"),
    ("Diploma Education", "Diploma Education"),
    ("Associate's Degree", "Associate's Degree"),
    ("Bachelor's Degree", "Bachelor's Degree"),
    ("Master's Degree", "Master's Degree"),
    ("Doctorate Degree (Ph.D)", "Doctorate Degree (Ph.D)"),
)
relationship_goals_choices = [
    ['A long-term relationship', 'A long-term relationship'],
    ['A life partner', 'A life partner'],
    ['Fun casual dates', 'Fun casual dates'],
    ['Intimacy, without commitment', 'Intimacy , without commitment'],
    ['Marriage', 'Marriage'],
    ['Ethical Non-monogamy', 'Ethical Non-monogamy'],
]
religion_choices = [
    ['Agnostic', 'Agnostic'], ['Atheist', 'Atheist'], ['Buddhist', 'Buddhist'],
    ['Catholic', 'Catholic'], ['Christian', 'Christian'], ['Hindu', 'Hindu'],
    ['Jewish', 'Jewish'], ['Morman', 'Morman'], ['Muslim', 'Muslim'],
    ['Latter-day Saint', 'Latter-day Saint'], ['Spiritual', 'Spiritual'],
]
politics_choices = [
    ['Apolitical', 'Apolitical'], ['Conservative', 'Conservative'],
    ['Liberal', 'Liberal'], ['Moderate', 'Moderate'],
]
body_choices = [
    ['Plus Size', 'Plus Size'], ['Slim', 'Slim'], ['Athletic', 'Athletic'], ['Curvy', 'Curvy'], ['Petite', 'Petite']
]
occupation_choices = [
    ['Accountant', 'Accountant'],
    ['Chef', 'Chef'],
    ['Civil Engineer', 'Civil Engineer'],
    ['Customer Service Rep', 'Customer Service Rep'],
    ['Data Analyst', 'Data Analyst'],
    ['Electrician', 'Electrician'],
    ['Financial Analyst', 'Financial Analyst'],
    ['Graphic Designer', 'Graphic Designer'],
    ['Human Resource', 'Human Resource'],
    ['Marketing', 'Marketing'],
    ['Mechanical Engineer', 'Mechanical Engineer'],
    ['Operations Manager', 'Operations Manager'],
    ['Pharmacist', 'Pharmacist'],
    ['Physical Therapist', 'Physical Therapist'],
    ['Registered Nurse', 'Registered Nurse'],
    ['Sale Representative', 'Sale Representative'],
    ['Socal Worker', 'Socal Worker'],
    ['Software Developer', 'Software Developer'],
    ['Surgeon', 'Surgeon'],
    ['Teacher', 'Teacher'],
    ['Web Developer', 'Web Developer'],
    ['Doctor', 'Doctor'],
]

class SettingPrivacyModel(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    opening_move = models.CharField(max_length=500, null=True)
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s setting and privacy"
    
    class Meta:
        verbose_name = 'Setting Privacy Model'
        verbose_name_plural = 'Setting Privacy Models'
    
    def model_details(self) -> Dict[str, str]:
        return {"Opening move": self.opening_move, "Bio": self.bio}

class MatchPreferenceModel(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    drinking = models.CharField(max_length=1, choices=habit_choices, null=True)
    smoking = models.CharField(max_length=1, choices=habit_choices, null=True)
    education_level = MultiSelectField(choices=education_choices, null=True)
    min_age = models.PositiveIntegerField(null=True)
    max_age = models.PositiveIntegerField(null=True)
    min_height = models.PositiveIntegerField(null=True)
    max_height = models.PositiveIntegerField(null=True)
    distance = models.PositiveIntegerField(null=True)
    relationship_goals = models.CharField(max_length=255, choices=relationship_goals_choices, null=True)
    occupation = MultiSelectField(choices=occupation_choices, null=True)
    body_build = MultiSelectField(choices=body_choices, null=True)
    religion = MultiSelectField(choices=religion_choices, null=True)
    politics = MultiSelectField(choices=politics_choices, null=True)
    setting = models.OneToOneField(SettingPrivacyModel, on_delete=models.CASCADE)

    def __str__(self):
        user = self.setting.user
        return f"{user.username}' match preference"

    class Meta:
        verbose_name = 'Match Preference Model'
        verbose_name_plural = 'Match Preference Models'
        
    def model_details(self) -> Dict[str, str]:
        return {
            "drinking": self.drinking, "smoking":self.smoking, "education level": self.education_level, "age": {"min age":self.min_age, "max age": self.max_age},
            "height": {
                "min height": self.min_height, "max height": self.max_height
            }, "distance": self.distance, "relationship goals": self.relationship_goals, "body build": self.body_build, "religion":self.religion, "Politics": self.politics
        }

class CausesModel(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    setting = models.ForeignKey(SettingPrivacyModel, on_delete=models.CASCADE)
    causes = models.TextField()
    
    def __str__(self,):
        user = self.setting.user
        return f"{user.username}'s causes and communities"
    
    class Meta:
        verbose_name = 'Cause and Community'
        verbose_name_plural = 'Cause and Communities'
        
    def model_details(self,) -> Dict[str, str]:
        return {"Cause":self.causes}
        
class QualitiesValueModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    setting = models.ForeignKey(SettingPrivacyModel, on_delete=models.CASCADE)
    quality = models.TextField()
    
    def __str__(self):
        user = self.setting.user
        return f"{user.username}'s values these quality "

    class Meta:
        verbose_name = 'Qualities and Value Model'
        verbose_name_plural = 'Qualities and Value Models'
        
    def model_details(self, ):
        return {"Quality": self.quality}
