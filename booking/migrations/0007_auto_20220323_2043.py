# Generated by Django 3.0.8 on 2022-03-23 15:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0042_auto_20220323_2041'),
        ('booking', '0006_feedback_event'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='feedback_event',
            new_name='feedback',
        ),
    ]
