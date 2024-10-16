# Generated by Django 5.0.6 on 2024-10-15 12:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app_root_security_user', '0019_alter_phonenumbersmodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppleGiftingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_apples', models.IntegerField(blank=True, null=True)),
                ('sender', models.EmailField(blank=True, max_length=254, null=True)),
                ('reciever', models.EmailField(blank=True, max_length=254, null=True)),
                ('reciever_accepts', models.BooleanField(blank=True, default=False, null=True)),
                ('reciever_rejects', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rotting_apples', models.FloatField(default=0, null=True)),
                ('apple_recieved', models.FloatField(default=0, null=True)),
                ('total_apple_sent', models.FloatField(default=0, null=True)),
                ('accepted_apple', models.FloatField(default=0, null=True)),
                ('is_expired', models.BooleanField(default=False, null=True)),
                ('bucket_of_apple', models.FloatField(default=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apple_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app_root_security_user.applemodel')),
                ('phone_number_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app_root_security_user.phonenumbersmodel')),
                ('user_auth_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_onboarding_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app_root_security_user.onboardinguserdetails')),
            ],
        ),
    ]
