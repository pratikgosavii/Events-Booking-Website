# Generated by Django 3.2.5 on 2021-10-30 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_rename_event_schedule_event_rounds'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event_Rounds',
            new_name='Event_Days',
        ),
    ]
