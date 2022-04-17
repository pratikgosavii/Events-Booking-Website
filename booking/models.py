from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from main.models import *

from django.conf import settings
User = settings.AUTH_USER_MODEL


# Create your models here.

UNKNWON_TYPE = 'UN'
payment_status_choices = [
        ('Pending', 'Pending'),
        ('Failed', 'Failed'),
        ('Processing', 'Processing'),
        ('Refunded', 'Refunded'),
        ('Done', 'Done'),
        
    ]


class event_ticket_booking(models.Model):
    owner =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_ticket')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='addsdgffgvgb')
    participants = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=11, choices=payment_status_choices, default=UNKNWON_TYPE)


class seminar_ticket_booking(models.Model):
    owner =  models.ForeignKey(User, on_delete=models.CASCADE,  related_name='seminar_lecsdture')
    seminar_lecture = models.ForeignKey(Seminar, on_delete=models.CASCADE, related_name='addsd')
    participants = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=11, choices=payment_status_choices, default=UNKNWON_TYPE)


class lecture_ticket_booking(models.Model):
    owner =  models.ForeignKey(User, on_delete=models.CASCADE,  related_name='seminarsd_lecture')
    participants = models.CharField(max_length=255)
    seminar_lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='addsdsd')
    payment_status = models.CharField(max_length=11, choices=payment_status_choices, default=UNKNWON_TYPE)

  

class feedback_answers(models.Model):

    user =  models.ForeignKey(User, on_delete=models.CASCADE,  related_name='wdedcsscd')
    event =  models.ForeignKey(Event, on_delete=models.CASCADE,  related_name='edfvsdefcesf')
    feeback_questions =  models.ForeignKey(feedback_questions, on_delete=models.CASCADE,  related_name='efesfszsfwe')
    stars = models.IntegerField()
  