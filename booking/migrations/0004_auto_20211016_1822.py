# Generated by Django 3.2.5 on 2021-10-16 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20211015_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture_ticket_booking',
            name='participants',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seminar_ticket_booking',
            name='participants',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
