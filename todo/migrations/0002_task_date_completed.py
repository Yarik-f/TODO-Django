# Generated by Django 4.2.17 on 2024-12-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_completed',
            field=models.DateTimeField(default='2025-01-01 17:00'),
        ),
    ]
