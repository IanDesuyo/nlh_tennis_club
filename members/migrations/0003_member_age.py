# Generated by Django 5.0 on 2023-12-13 05:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0002_auto_20230301_0430"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="age",
            field=models.IntegerField(null=True),
        ),
    ]
