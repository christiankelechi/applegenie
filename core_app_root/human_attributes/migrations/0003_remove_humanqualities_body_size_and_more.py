# Generated by Django 4.2.13 on 2024-06-10 00:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "core_app_root_human_attributes",
            "0002_rename_shirt_size_humanqualities_body_size",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="humanqualities",
            name="body_size",
        ),
        migrations.RemoveField(
            model_name="humanqualities",
            name="hobbies",
        ),
        migrations.RemoveField(
            model_name="humanqualities",
            name="is_hot_tempered",
        ),
        migrations.RemoveField(
            model_name="humanqualities",
            name="skin_color",
        ),
        migrations.AddField(
            model_name="humanqualities",
            name="age",
            field=models.IntegerField(default=18),
        ),
        migrations.AddField(
            model_name="humanqualities",
            name="country",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name="humanqualities",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[
                    ("male", "Male"),
                    ("female", "Female"),
                    ("not specified", "Not specified"),
                ],
                max_length=1000,
                null=True,
            ),
        ),
    ]