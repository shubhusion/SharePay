# Generated by Django 4.2.4 on 2023-08-06 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("smartsplit", "0009_remove_friendrequests_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="FriendList",
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
                ("friend_id", models.IntegerField(default=0)),
                ("friend_username", models.CharField(default="", max_length=100)),
                (
                    "this_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]