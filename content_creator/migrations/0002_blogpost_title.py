# Generated by Django 5.0.6 on 2024-09-09 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content_creator", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="title",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
