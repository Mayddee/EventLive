# Generated by Django 5.0.4 on 2024-05-02 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_available_seats_event_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='available_seats',
            field=models.IntegerField(default=1),
        ),
    ]
