# Generated by Django 4.2.13 on 2024-06-16 14:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "core_app_root_human_attributes",
            "0003_remove_humanqualities_body_size_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="HumanInterests",
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
                ("nature", models.BooleanField(default=False)),
                ("travel", models.BooleanField(default=False)),
                ("writing", models.BooleanField(default=False)),
            ],
        ),
    ]