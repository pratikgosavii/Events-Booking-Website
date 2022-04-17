
from logging import PlaceHolder
from django.forms import ModelForm
from django.forms import widgets
from django.forms.fields import DateTimeField
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import *


## 
# child form
##
class Event_form(ModelForm):

    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['created_by', 'number_of_days']\

class Event_Days_form(ModelForm):

    class Meta:
        model = Event_Days
        fields = '__all__'
        exclude = ['event']
        

class Day_details_form(ModelForm):

    class Meta:
        model = Day_Schedule
        fields = '__all__'
        exclude = ['day', 'start_date', 'end_date']
       

class Event_Prices_form(ModelForm):

    class Meta:
        model = Event_Prices
        fields = '__all__'
        widgets = {
            'event': forms.Select(attrs={
                'class': 'form-control input-group mb-3 get', 'id': 'bike', 'placeholder': 'Event'
            }),
            'rank': forms.Select(attrs={
                'class': 'form-control input-group mb-3 get', 'id': 'showroom'
            }),
            'user': forms.Select(attrs={
                'class': 'form-control input-group mb-3 get', 'id': 'bike_qty', 'placeholder': 'Event'
            }),
            'prize': forms.NumberInput(attrs={
                'class': 'form-control input-group mb-3 get', 'id': 'bike_qty', 'placeholder': 'Event'
            }),

            
        }       
        

class Seminar_form(ModelForm):

    class Meta:
        model = Seminar
        fields = '__all__'
        exclude = ['created_by', 'number_of_days']





class feedback_questions_Form(ModelForm):

    class Meta:
        model = feedback_questions
        fields = '__all__'
        exclude = ['event']
        # format = '%Y-%m-%dT%H:%M'),