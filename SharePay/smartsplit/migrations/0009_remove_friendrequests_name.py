# Generated by Django 4.2.4 on 2023-08-05 23:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("smartsplit", "0008_friendrequests_friend_id_friendrequests_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="friendrequests",
            name="name",
        ),
    ]