# Generated by Django 5.0.6 on 2024-08-16 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app_root_image_kyc', '0002_rename_userimagekwc_userimagekyc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimagekyc',
            name='user_default_image',
            field=models.FileField(blank=True, null=True, upload_to='kyc_images'),
        ),
        migrations.AlterField(
            model_name='userimagekyc',
            name='user_real_time_capture',
            field=models.FileField(blank=True, null=True, upload_to='kyc_images'),
        ),
    ]
