# Generated by Django 3.0.8 on 2022-03-23 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_auto_20220323_2041'),
        ('booking', '0007_auto_20220323_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='stars',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='feedback_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fed_questions', models.CharField(max_length=255)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wfdsddxd', to='main.Event')),
            ],
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feeback_questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='efesfszsfwe', to='booking.feedback_questions'),
        ),
    ]
