# Generated by Django 4.2.13 on 2024-06-10 00:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core_app_root_chat_management", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatclientmodel",
            name="prompt_message",
            field=models.TextField(
                choices=[
                    (
                        "What activities do you enjoy in your free time?",
                        "What activities do you enjoy in your free time?",
                    ),
                    (
                        "Do you have any favorite books, movies, or TV shows?",
                        "Do you have any favorite books, movies, or TV shows?",
                    ),
                    (
                        "What are you looking for in a relationship?",
                        "What are you looking for in a relationship?",
                    ),
                    ("Describe your ideal partner.", "Describe your ideal partner."),
                    (
                        "How do you typically spend your weekends?",
                        "How do you typically spend your weekends?",
                    ),
                    (
                        "What values are most important to you in a partner?",
                        "What values are most important to you in a partner?",
                    ),
                    (
                        "Do you enjoy traveling? If so, what's your favorite destination?",
                        "Do you enjoy traveling? If so, what's your favorite destination?",
                    ),
                    (
                        "Are you more of a beach person or a mountain person?",
                        "Are you more of a beach person or a mountain person?",
                    ),
                    (
                        "Do you prefer nights out or cozy evenings at home?",
                        "Do you prefer nights out or cozy evenings at home?",
                    ),
                    (
                        "What's your favorite type of cuisine?",
                        "What's your favorite type of cuisine?",
                    ),
                    (
                        "Tell us a bit about your background and upbringing.",
                        "Tell us a bit about your background and upbringing.",
                    ),
                    (
                        "Are there any cultural traditions that are important to you?",
                        "Are there any cultural traditions that are important to you?",
                    ),
                    (
                        "Where do you see yourself in the next five years?",
                        "Where do you see yourself in the next five years?",
                    ),
                    (
                        "What are some goals you are currently working towards?",
                        "What are some goals you are currently working towards?",
                    ),
                    (
                        "If you could have dinner with any historical figure, who would it be and why?",
                        "If you could have dinner with any historical figure, who would it be and why?",
                    ),
                    (
                        "What's a fun fact about you that most people don't know?",
                        "What's a fun fact about you that most people don't know?",
                    ),
                    (
                        "What type of apple best describes your personality and why?",
                        "What type of apple best describes your personality and why?",
                    ),
                    (
                        "If you could gift an apple to anyone in history, who would it be and why?",
                        "If you could gift an apple to anyone in history, who would it be and why?",
                    ),
                ]
            ),
        ),
    ]
