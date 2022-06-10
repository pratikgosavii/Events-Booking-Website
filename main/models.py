from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms.fields import DateField

from django.conf import settings
User = settings.AUTH_USER_MODEL


# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to="media/", null=False, blank=False)
    min_participants = models.IntegerField()
    max_participants = models.IntegerField()
    hod = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    number_of_days = models.IntegerField()

    first_price_money  = models.IntegerField()
    second_price_money  = models.IntegerField()
    third_price_money  = models.IntegerField()

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    event_cordinator = models.CharField(max_length=555)
    
    description = models.CharField(max_length=555)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sdscscs')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)


class Event_Days(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='sdsk')
    title = models.CharField(max_length=255, null = True)
    sub_title = models.CharField(max_length=255, null = True)
    start_date = models.DateTimeField(default=timezone.now, null = True)
    end_date = models.DateTimeField(default=timezone.now, null = True)
    description = models.CharField(max_length=255, null = True)

class Day_Schedule(models.Model):

    day = models.ForeignKey(Event_Days, on_delete=models.CASCADE, related_name='sdsddsd')
    title = models.CharField(max_length=255, null = True)
    start_date = models.DateTimeField(default=timezone.now, null = True)
    end_date = models.DateTimeField(default=timezone.now, null = True)
    description = models.CharField(max_length=555, null = True)

rank_CHOICES = (
        ('First', 'First'),
        ('Second', 'Second'),
        ('Third', 'Third'),
    )
    
class Event_Prices(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='sdsdsadc')
    rank = models.CharField(max_length=343, choices=rank_CHOICES)
    user  =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='dfdf')
    prize = models.IntegerField()


class Seminar(models.Model):

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to="media/", null=False, blank=False)
    hod = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    number_of_days = models.IntegerField()
    speaker = models.CharField(max_length=500)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    event_cordinator = models.CharField(max_length=555)
    
    description = models.CharField(max_length=555)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sdsd')
    created_at = models.DateTimeField(auto_now=True)



class Seminar_Days(models.Model):

    seminar = models.ForeignKey(Seminar, on_delete=models.CASCADE, related_name='sd')
    title = models.CharField(max_length=255, null = True)
    sub_title = models.CharField(max_length=255, null = True)
    start_date = models.DateTimeField(default=timezone.now, null = True)
    end_date = models.DateTimeField(default=timezone.now, null = True)
    description = models.CharField(max_length=255, null = True)

class Seminar_Day_Schedule(models.Model):

    day = models.ForeignKey(Seminar_Days, on_delete=models.CASCADE, related_name='sd')
    title = models.CharField(max_length=255, null = True)
    start_date = models.DateTimeField(default=timezone.now, null = True)
    end_date = models.DateTimeField(default=timezone.now, null = True)
    description = models.CharField(max_length=555, null = True)


class Lecture(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to="images/")

    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    lecturer_name = models.CharField(max_length=255, default='abc')

    lecturer_description = models.CharField(max_length=555)

    event_leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addwdfwedsddsa')
    
    description = models.CharField(max_length=555)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dfdefwed')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)




class teachers_form(models.Model):

    description = models.CharField(max_length=2555)
    name = models.CharField(max_length=255)
    department =  models.CharField(max_length=255)
    image1 = models.ImageField(upload_to="images/")
    image2 = models.ImageField(upload_to="images/")
    collage = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)

    lecturer_name = models.CharField(max_length=255, default='abc')

    lecturer_description = models.CharField(max_length=555)

    event_leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addddsa')
    
    description = models.CharField(max_length=555)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asffddfdfd')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)









class feedback_questions(models.Model):

    event =  models.ForeignKey(Event, on_delete=models.CASCADE,  related_name='wfdsddxd')
    fed_questions =  models.CharField(max_length=255)
  
  