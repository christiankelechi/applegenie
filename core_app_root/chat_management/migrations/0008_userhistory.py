# Generated by Django 5.0.6 on 2024-07-23 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app_root_chat_management', '0007_questionandanswer_email_storeuserchatmodel_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('user_questions', models.TextField(blank=True, null=True)),
                ('genie_response_to_user', models.TextField(blank=True, null=True)),
                ('genie_suggestions_questions', models.TextField(blank=True, null=True)),
                ('user_response_to_genie', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
