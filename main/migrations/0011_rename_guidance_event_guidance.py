# Generated by Django 3.2.5 on 2021-10-17 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_event_guidance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='Guidance',
            new_name='guidance',
        ),
    ]
