# Generated by Django 3.2.9 on 2022-02-12 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chousei", "0002_set_event_properties_20220212_1408"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="slack_notification_user",
            field=models.TextField(
                blank=True, default="", verbose_name="Slack 通知先ユーザー名"
            ),
        ),
    ]