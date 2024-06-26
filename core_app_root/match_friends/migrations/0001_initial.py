# Generated by Django 4.2.13 on 2024-06-10 00:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserAttributes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
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
                ("age", models.IntegerField(max_length=1000)),
                ("country", models.CharField(max_length=10000)),
            ],
        ),
    ]
