# Generated by Django 4.1.7 on 2023-06-09 05:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shortener", "0009_backofficelogs"),
    ]

    operations = [
        migrations.CreateModel(
            name="Schedules",
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
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("job_name", models.CharField(max_length=50)),
                ("flag_name", models.CharField(max_length=50)),
                ("value", models.IntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
