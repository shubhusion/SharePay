# Generated by Django 4.2 on 2023-08-01 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(default='', max_length=100)),
                ('message', models.CharField(default='', max_length=200)),
                ('request_amount', models.FloatField(default=0.0, max_length=100)),
                ('recipient', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(default='', max_length=100)),
                ('message', models.CharField(default='', max_length=100)),
                ('request_amount', models.FloatField(default=0.0, max_length=100)),
                ('recipient', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
