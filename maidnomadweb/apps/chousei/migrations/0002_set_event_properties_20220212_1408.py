# Generated by Django 3.2.9 on 2022-02-12 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chousei", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="event",
            options={
                "ordering": ["pk"],
                "verbose_name": "イベント",
                "verbose_name_plural": "イベント",
            },
        ),
        migrations.AlterModelOptions(
            name="eventdate",
            options={
                "ordering": ["pk"],
                "verbose_name": "イベント候補日",
                "verbose_name_plural": "イベント候補日",
            },
        ),
        migrations.AlterModelOptions(
            name="eventperson",
            options={
                "ordering": ["pk"],
                "verbose_name": "イベント参加者",
                "verbose_name_plural": "イベント参加者",
            },
        ),
        migrations.AlterModelOptions(
            name="schedule",
            options={
                "ordering": ["pk"],
                "verbose_name": "スケジュール回答",
                "verbose_name_plural": "スケジュール回答",
            },
        ),
        migrations.AlterField(
            model_name="eventperson",
            name="comment",
            field=models.TextField(blank=True, verbose_name="コメント"),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="answer",
            field=models.IntegerField(
                choices=[(2, "○"), (1, "△"), (0, "×")], verbose_name="回答"
            ),
        ),
    ]