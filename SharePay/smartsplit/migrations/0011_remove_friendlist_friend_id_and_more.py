# Generated by Django 4.2.4 on 2023-08-06 14:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("smartsplit", "0010_friendlist"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="friendlist",
            name="friend_id",
        ),
        migrations.RemoveField(
            model_name="friendrequests",
            name="friend_id",
        ),
    ]
