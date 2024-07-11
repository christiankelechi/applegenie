from django.db import models
from core_app_root.security.user.models import User
# Create your models here.
class ChatClientModel(models.Model):
    # Choices for prompt_message
    WHAT_ACTIVITIES_DO_YOU_ENJOY = 'What activities do you enjoy in your free time?'
    FAVORITE_BOOKS_MOVIES_TV_SHOWS = 'Do you have any favorite books, movies, or TV shows?'
    WHAT_ARE_YOU_LOOKING_FOR = 'What are you looking for in a relationship?'
    IDEAL_PARTNER = 'Describe your ideal partner.'
    WEEKENDS = 'How do you typically spend your weekends?'
    VALUES_IN_PARTNER = 'What values are most important to you in a partner?'
    TRAVELING = 'Do you enjoy traveling? If so, what\'s your favorite destination?'
    BEACH_OR_MOUNTAIN = 'Are you more of a beach person or a mountain person?'
    NIGHTS_OUT_OR_COZY_EVENINGS = 'Do you prefer nights out or cozy evenings at home?'
    FAVORITE_CUISINE = 'What\'s your favorite type of cuisine?'
    BACKGROUND_UPBRINGING = 'Tell us a bit about your background and upbringing.'
    CULTURAL_TRADITIONS = 'Are there any cultural traditions that are important to you?'
    FIVE_YEARS = 'Where do you see yourself in the next five years?'
    CURRENT_GOALS = 'What are some goals you are currently working towards?'
    DINNER_WITH_HISTORICAL_FIGURE = 'If you could have dinner with any historical figure, who would it be and why?'
    FUN_FACT = 'What\'s a fun fact about you that most people don\'t know?'
    APPLE_PERSONALITY = 'What type of apple best describes your personality and why?'
    GIFT_TO_HISTORY = 'If you could gift an apple to anyone in history, who would it be and why?'

    # Choices for prompt_message
    list_of_questions = [
        (WHAT_ACTIVITIES_DO_YOU_ENJOY, 'What activities do you enjoy in your free time?'),
        (FAVORITE_BOOKS_MOVIES_TV_SHOWS, 'Do you have any favorite books, movies, or TV shows?'),
        (WHAT_ARE_YOU_LOOKING_FOR, 'What are you looking for in a relationship?'),
        (IDEAL_PARTNER, 'Describe your ideal partner.'),
        (WEEKENDS, 'How do you typically spend your weekends?'),
        (VALUES_IN_PARTNER, 'What values are most important to you in a partner?'),
        (TRAVELING, 'Do you enjoy traveling? If so, what\'s your favorite destination?'),
        (BEACH_OR_MOUNTAIN, 'Are you more of a beach person or a mountain person?'),
        (NIGHTS_OUT_OR_COZY_EVENINGS, 'Do you prefer nights out or cozy evenings at home?'),
        (FAVORITE_CUISINE, 'What\'s your favorite type of cuisine?'),
        (BACKGROUND_UPBRINGING, 'Tell us a bit about your background and upbringing.'),
        (CULTURAL_TRADITIONS, 'Are there any cultural traditions that are important to you?'),
        (FIVE_YEARS, 'Where do you see yourself in the next five years?'),
        (CURRENT_GOALS, 'What are some goals you are currently working towards?'),
        (DINNER_WITH_HISTORICAL_FIGURE, 'If you could have dinner with any historical figure, who would it be and why?'),
        (FUN_FACT, 'What\'s a fun fact about you that most people don\'t know?'),
        (APPLE_PERSONALITY, 'What type of apple best describes your personality and why?'),
        (GIFT_TO_HISTORY, 'If you could gift an apple to anyone in history, who would it be and why?')
    ]

    prompt_message = models.TextField(choices=list_of_questions)
    
    def get_list_of_questions(self):
        return [(choice[0], choice[1]) for choice in self.list_of_questions]
    

class StoreUserChatModel(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    suggestion_question=models.TextField(null=True,blank=True)
    user_response=models.TextField(null=True,blank=True)

    
    # def __str__(self):
    #     return f"{self.user} successfully answered the apple match suggestion question "
    

class QuestionAndAnswer(models.Model):
    prompt_in=models.TextField(null=True,blank=True)
    prompt_output=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.user} question stored successfully "