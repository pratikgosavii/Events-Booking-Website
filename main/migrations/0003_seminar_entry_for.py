# Generated by Django 3.2.5 on 2021-10-12 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211013_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminar',
            name='entry_for',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('More', 'More than 5')], default=1, max_length=255),
        ),
    ]
