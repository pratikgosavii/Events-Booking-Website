# Generated by Django 3.2.5 on 2021-10-30 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_day_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event_Schedule',
            new_name='Event_Rounds',
        ),
    ]
