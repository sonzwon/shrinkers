# Generated by Django 4.1.7 on 2023-05-08 04:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shortener", "0006_statistic_custom_params_trackingparams"),
    ]

    operations = [
        migrations.RenameField(
            model_name="trackingparams",
            old_name="Shortened_url",
            new_name="shortened_url",
        ),
    ]