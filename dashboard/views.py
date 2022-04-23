from pydoc import describe
from django.db.models.query import InstanceCheckMeta
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from main.models import *
from main.forms import *
import numpy as np
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from datetime import date

import pytz
ist = pytz.timezone('Asia/Kolkata')



# Create your views here.


#event view add update delete

def index(request):

    return render(request, 'index.html')

@csrf_exempt
def test(request):

    if request.method == 'POST':

        a = request.POST.get('arr[]')
        print(a)

    else:
        return render(request, 'staff/event/test.html')


def staff_dashbaord(request):

     
    Event_data = Event.objects.filter(created_by=request.user)
    event_count = Event.objects.all().count()

    return render(request, 'staff/dashboard.html', {'data':Event_data, 'event_count':event_count})


def show_event(request):

    data = Event.objects.filter(created_by = request.user)
    print('id')
    if data:
        event_id = (data[0].id)
    else:
        event_id = None
    if data:

        return render(request, 'staff/event/show_events.html', {'data':data, 'event_id':event_id})
    else:
        
        messages.info(request, "You don't have any event registerd please register one")
        return HttpResponseRedirect(reverse('add_event'))

def numOfDays(date1, date2):


    print('from here')
    print(date1, date2)

    dt1 = date1.split('T')

    dt1 = dt1[0]

    print(dt1)

    


    dt2 = date2.split('T')
    dt2 = dt2[0]

    print(dt2)



    print(dt2)

    d1 = dt1.split('-')
    d2 = dt2.split('-')

    date1 = date(int(d1[0]), int(d1[1]), int(d1[2]))
    date2 = date(int(d2[0]), int(d2[1]), int(d2[2]))

    print('----------------------------------------')
    print(date1, date2)

    
    return (date2-date1).days



def format_fDate(date1):

    dt1 = date1.split('T')

    time = dt1[1]
    time1 = time.split(':')

    dt1 = dt1[0]
    
    dt1 = dt1.split('-')
    

    year = int(dt1[0])
    month = int(dt1[1])
    day = int(dt1[2])

    date1 = datetime(year,month, day , int(time1[0]), int(time1[1]), tzinfo=ist)

    print('--------------')
    print(date1)
    return date1


def add_event(request):
    
    if request.method == 'POST':

        dt1 = request.POST.get('start_date')

        dt2 = request.POST.get('end_date')

        

        start_date = format_fDate(dt1)
        end_date = format_fDate(dt2)

        print('----------here---------------')
        print(start_date)
        print(end_date)

        

        updated_request = request.POST.copy()
        updated_request.update({'start_date': start_date, 'end_date' : end_date})
        form = Event_form(updated_request, request.FILES)


        if form.is_valid():

            dt1 = request.POST.get('start_date')
           
            dt2 = request.POST.get('end_date')
           
           
        
            number_of_days = numOfDays(dt1, dt2)
            print('--------------------------------------')
            print(number_of_days)

            instance = form.save(commit=False)
            instance.created_by = request.user

            instance.number_of_days = number_of_days

            instance.save()
            print('save')
            

            counter_title = 1

            for i in range(instance.number_of_days):
                title = 'Day ' + str(counter_title)
                today = datetime.now()
                d1 = today.strftime("%Y-%m-%d") + 'T'
                d2=today.strftime("%H:%I")
                d3 = d1+d2
                Event_Days.objects.create(event = instance, title = title, sub_title = 'NA', start_date = d3, end_date = d3, description = 'NA') 
                counter_title = counter_title + 1

            data = Event_Days.objects.filter(event = instance)
            return render(request, 'staff/event/add_days.html', {'data':data, 'event_id':instance.id})

        else:
            print(form.errors)

            data = Event.objects.filter(created_by = request.user)
            return render(request, 'staff/event/add_event.html', {'data':data})

    else:
        form = Event_form()

        Event_data = Event.objects.filter(created_by=request.user)
        return render(request, 'staff/event/add_event.html', {'data':Event_data, 'form':form})

def view_event(request, event_id):

    instance = Event.objects.get(id = event_id)
    form = Event_form(instance=instance)

    return render(request, 'staff/event/update_event.html', {'form':form, 'event_id':event_id, 'update':False})


def update_event(request, event_id=None):

    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        instance = Event.objects.get(id = event_id)
        form  = Event_form(request.POST, request.FILES, instance = instance)
        
        a = request.POST.get('end_date')
    
        if form.is_valid():

            dt1 = request.POST.get('start_date')
            dt2 = request.POST.get('end_date')
            number_of_days = numOfDays(dt1, dt2)

            if number_of_days != number_of_days:

                instance = form.save(commit=False)
                
                instance.number_of_days = number_of_days

                instance.save()
                print('save')
                instance = Event.objects.get(id = event_id)
                form = Event_form(instance=instance)

                return render(request, 'staff/event/update_event.html', {'form':form, 'update':True, 'event_id':event_id})

            else:

                form.save()
                print('save')
                instance = Event.objects.get(id = event_id)
                data = Event_Days.objects.filter(event = instance)
                return render(request, 'staff/event/add_days.html', {'data':data, 'event_id':event_id, 'popup':True})


        else:

            print(form.errors)

            instance = Event.objects.get(id = event_id)
            form = Event_form(instance=instance)
            return render(request, 'staff/event/update_event.html', {'form':form, 'update':True})

    else:

        instance = Event.objects.get(id = event_id)
        form = Event_form(instance=instance)
        print(instance.start_date)

        return render(request, 'staff/event/update_event.html', {'form':form, 'event_id':event_id, 'update':True})


def delete_event(request, event_id):
    
    instance = Event.objects.get(id = event_id).delete()
    if instance:
        
        data = Event.objects.filter(created_by = request.user)
        
        return render(request, 'staff/event/show_events.html', {'data':data})

    else:
        print('something went wrong')
        data = Event.objects.filter(created_by = request.user)

        return render(request, 'staff/event/add_event.html', {'data':data})



from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import magenta, red
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import subprocess
import os
from django.http import FileResponse, Http404



def add_form(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        print(title)
        description = request.POST.get('describe')
        name = request.POST.get('name')
        department = request.POST.get('department')
        collage = request.POST.get('collage')
        date = request.POST.get('date')

        

   
        def genpdf():
            doc = SimpleDocTemplate("hello.pdf")
            parts = []
            txt = description
            PAGE_WIDTH, PAGE_HEIGHT = A4
            style = ParagraphStyle(name='Times New Roman')
            style.fontSize = 12
            style.leading = 20
            p = Paragraph(txt, style)
            style1 = ParagraphStyle(name='Times New Roman')
            style1.fontSize = 16
            style1.leading = 20
            style1.textColor = 'black'
            style1.alignment = TA_CENTER
            q=Paragraph(title, style1)

            style2 = ParagraphStyle(name='Times New Roman')
            style2.fontSize = 14
            style2.leading = 20
            style2.textColor = 'black'
            style2.alignment = TA_LEFT

            txt2 = '<br />\n<br />\n<br />\n<br />\n<br />\n' + 'Details of program cordinator' + '<br />\n' + name + '<br />\n' + department + '<br />\n' + collage + '<br />\n' + date

            print(txt2)

            x = Paragraph(txt2, style2)
            parts.append(q)
            parts.append(p)
            parts.append(x)
            doc.build(parts)
        genpdf()

        return FileResponse(open('hello.pdf', 'rb'), content_type='application/pdf')
    else:
        return render(request, 'staff/teacher_submit_form.html')

def add_event_winner(request):
    
    if request.method == 'POST':

        form  = Event_Prices_form(request.POST, request.FILES)

        data = Event_Prices.objects.all()

        if form.is_valid():
           
            form.save()

            return render(request, 'staff/event/show_event_winner.html', {'data':data})

        else:
            print(form.errors)
            return render(request, 'staff/event/add_event_winner.html', {'data':data})

    else:
        form = Event_Prices_form()

        Event_data = Event.objects.filter(created_by=request.user)
        return render(request, 'staff/event/add_event_winner.html', {'data':Event_data, 'form':form})


def update_event_winner(request, event_id=None):

    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        instance = Event.objects.get(id = event_id)
        form  = Event_form(request.POST, request.FILES, instance = instance)
        
        a = request.POST.get('end_date')
    
        if form.is_valid():

            dt1 = request.POST.get('start_date')
            dt2 = request.POST.get('end_date')
            number_of_days = numOfDays(dt1, dt2)

            if number_of_days != number_of_days:

                instance = form.save(commit=False)
                
                instance.number_of_days = number_of_days

                instance.save()
                print('save')
                instance = Event.objects.get(id = event_id)
                form = Event_form(instance=instance)

                return render(request, 'staff/event/update_event.html', {'form':form, 'update':True, 'event_id':event_id})

            else:

                form.save()
                print('save')
                instance = Event.objects.get(id = event_id)
                data = Event_Days.objects.filter(event = instance)
                return render(request, 'staff/event/add_days.html', {'data':data, 'event_id':event_id, 'popup':True})


        else:

            print(form.errors)

            instance = Event.objects.get(id = event_id)
            form = Event_form(instance=instance)
            return render(request, 'staff/event/update_event.html', {'form':form, 'update':True})

    else:

        instance = Event.objects.get(id = event_id)
        form = Event_form(instance=instance)
        print(instance.start_date)

        return render(request, 'staff/event/update_event.html', {'form':form, 'event_id':event_id, 'update':True})


def delete_event_winner(request, event_id):
    
    instance = Event.objects.get(id = event_id).delete()
    if instance:
        
        data = Event.objects.filter(created_by = request.user)
        
        return render(request, 'staff/event/show_events.html', {'data':data})

    else:
        print('something went wrong')
        data = Event.objects.filter(created_by = request.user)

        return render(request, 'staff/event/add_event.html', {'data':data})


def show_event_winner(request):

    data = Event_Prices.objects.all()
    print('id')
    if data:

        return render(request, 'staff/event/show_event_winner.html', {'data':data})
    else:
        
        messages.info(request, "You don't have any event registerd please register one")
        return HttpResponseRedirect(reverse('add_event_winner'))



#day schedue

def show_days(request, event_id):

    instance = Event.objects.get(id = event_id)
    data = Event_Days.objects.filter(event = instance)
    return render(request, 'staff/event/add_days.html', {'data':data, 'event_id':event_id})

def add_day(request, event_id):

    if event_id:

        a = Event.objects.get(id = event_id)

        title = 'Day ' + str((a.number_of_days + int(1)))
        today = datetime.now()
        d1 = today.strftime("%Y-%m-%d") + 'T'
        d2=today.strftime("%H:%I")
        d3 = d1+d2
        test = Event_Days.objects.create(event = a, title = title, sub_title = 'NA', start_date = d3, end_date = d3, description = 'NA') 
        if test:
            a.number_of_days =  a.number_of_days + int(1)
            a.save()
            data = Event_Days.objects.filter(event = a)
            msg = 'Day number ' + str(a.number_of_days)  + ' added successfully'
            print(msg)
            return render(request, 'staff/event/add_days.html', {'data':data, 'event_id':event_id})

        else:
            print('something went wrong')
            data = Event_Days.objects.filter(event = a)
            return render(request, 'staff/event/add_days.html', {'data':data, 'event_id':event_id})

    # else:
    #     print('something went wrong')
    #     data = Event.objects.filter(created_by = request.user)
    #     return render(request, 'staff/event/add_day.html', {'data':data})


def view_details_day(request, day_id):

    data = Event_Days.objects.get(id = day_id)
    instance = Event_Days_form(instance = data)
    event_id = data.event.id
    
    return render(request, 'staff/event/update_day.html', {'form':instance, 'event_id':event_id, 'day_id':day_id, 'update':True})


    

def update_day(request, day_id=None):

    if request.method == 'POST':

        instance = Event_Days.objects.get(id = day_id)

        dt1 = request.POST.get('start_date')

        dt2 = request.POST.get('end_date')


        start_date = format_fDate(dt1)
        end_date = format_fDate(dt2)

        updated_request = request.POST.copy()
        updated_request.update({'start_date': start_date, 'end_date' : end_date})
        form = Event_Days_form(updated_request, request.FILES, instance=instance)

        if form.is_valid():
            form.save()

            event_id = instance.event.id

            instance = Event_Days_form(instance = instance)
            return render(request, 'staff/event/update_day.html', {'form':instance,'event_id':event_id, 'day_id':day_id, 'update':True})

        else:
            print(form.errors)
            instance = Event_Days.objects.get(id = day_id)
            event_id = instance.event.id
            instance = Event_Days_form(instance = instance)

            return render(request, 'staff/event/update_day.html', {'form':instance, 'update':True})
            return render(request, 'staff/event/update_day.html', {'form':instance, 'update':True, 'day_id':day_id,'event_id':event_id})


    else:

        instance = Event_Days.objects.get(id = day_id)
        event_id = instance.event.id

        form = Event_Days_form(instance=instance)
        
        return render(request, 'staff/event/update_day.html', {'form':form, 'event_id':event_id, 'day_id':day_id, 'update':True})

def delete_day(request, event_id):

    instance = Event.objects.get(id = event_id)
    instance.number_of_days =  instance.number_of_days - int(1)
    instance.save()

    Event_Days.objects.filter(event = instance).last().delete()

    data = Event_Days.objects.filter(event = instance)
    
    return render(request, 'staff/event/add_days.html', {'data':data, 'event_id':event_id})




#day schedule
def show_day_schedule(request, day_id):

    day = Event_Days.objects.get(id = day_id)
    data = Day_Schedule.objects.filter(day = day)
   
    event_id = day.event.id
    return render(request, 'staff/event/show_days_schedule.html', {'data': data, 'event_id':event_id, 'day_id':day_id})

def add_day_schedule_form(request, day_id):

    return render(request, 'staff/event/add_days_details.html', {'day_id':day_id})

def add_day_schedule(request, day_id):

    if request.method == 'POST':
        a = day_id
        print(a)
        day = Event_Days.objects.get(id=a)
        print(day)
        form = Day_details_form(request.POST)

        if form.is_valid():

            instance = form.save(commit=False)
            instance.day = day
            instance.save()

        else:
            print(form.errors)

        data = Day_Schedule.objects.filter(day = day)
        event_id = day.event.id


        return render(request, 'staff/event/show_days_schedule.html', {'data': data, 'event_id':event_id, 'day_id':a})
    
    




def day_schedule_details(request, day_schedule_id):

    instance = Day_Schedule.objects.get(id = day_schedule_id)
    day_id = instance.day.id
    event_id = instance.day.event.id

    form = Day_details_form(instance=instance)
    return render(request, 'staff/event/update_day_schedule.html', {'form':form, 'update':False, 'event_id':event_id, 'day_id':day_id, 'day_schedule_id':day_schedule_id, })

def view_day_schedule(request, day_schedule_id):
    instance = Day_Schedule.objects.get(id = day_schedule_id)
    event_id = instance.day.event.id

    day_id = instance.day.id
    form = Day_details_form(instance=instance)
    return render(request, 'staff/event/update_day_schedule.html', {'form':form, 'update':False, 'event_id':event_id, 'day_id':day_id, 'day_schedule_id':day_schedule_id})


def update_day_schedule(request, day_schedule_id):

    day = Day_Schedule.objects.get(id=day_schedule_id)
    event_id = day.day.event.id


    if request.method == 'POST':

        
        form = Day_details_form(request.POST, instance = day)

        if form.is_valid():

            form.save()

            print(form.errors)
            form = Day_details_form(instance = day)
            day_id = day.day.id

            return render(request, 'staff/event/update_day_schedule.html', {'form':form, 'update':True, 'event_id':event_id, 'day_id':day_id, 'day_schedule_id':day_schedule_id})

    else:

        instance = Day_Schedule.objects.get(id = day_schedule_id)
        form = Day_details_form(instance=instance)
        day_id = day.day.id

        return render(request, 'staff/event/update_day_schedule.html', {'form':form, 'update':True, 'event_id':event_id, 'day_id':day_id, 'day_schedule_id':day_schedule_id})



def day_schedule_delete(request, day_schedule_id):
    
    aa = Day_Schedule.objects.get(id=day_schedule_id)
    event_id = aa.day.event.id


    
    if aa:
        day_id = aa.day.id
        day = Event_Days.objects.get(id = day_id)
        data = Day_Schedule.objects.filter(day = day)
        a = Day_Schedule.objects.get(id=day_schedule_id).delete()
        
        return render(request, 'staff/event/show_days_schedule.html', {'data': data, 'event_id':event_id, 'day_id':day_id})
    else:

        # reverse (show day schedule)
        pass


from django.shortcuts import render
from .models import QrCode
# Create your views here.
def generate_gr(request, event_id):

    domain = (request.META['HTTP_HOST'])
   
    url = reverse('event_details', kwargs={'event_id':event_id})
    Event.objects.get(id = event_id)
    
    Url = str(domain) + str(url)
    print(Url)
    QrCode.objects.create(url=Url)

    qr_code=QrCode.objects.all().last()
    return render(request,"generated_qr.html",{'qr_code':qr_code})


def show_seminars(request):
    pass

def add_seminars(request):

    if request.method == 'POST':

        form  = Seminar_form(request.POST, request.FILES)
        if form.is_valid():
            dt1 = request.POST.get('start_date')
           
            dt2 = request.POST.get('end_date')

           
            number_of_days = numOfDays(dt1, dt2)
            print('--------------------------------------')
            print(number_of_days)

            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.number_of_days = number_of_days

            instance.save()
            print('save')
            

            counter_title = 1

            for i in range(instance.number_of_days):
                title = 'Day ' + str(counter_title)
                today = datetime.now()
                d1 = today.strftime("%Y-%m-%d") + 'T'
                d2=today.strftime("%H:%I")
                d3 = d1+d2
                Seminar_Days.objects.create(event = instance, title = title, sub_title = 'NA', start_date = d3, end_date = d3, description = 'NA') 
                counter_title = counter_title + 1

            data = Seminar_Days.objects.filter(event = instance)
            return render(request, 'staff/seminar/add_days.html', {'data':data, 'event_id':instance.id})

        else:
            print(form.errors)
            data = Seminar.objects.filter(created_by = request.user)
            return render(request, 'staff/seminar/add_seminar.html', {'data':data})

    else:
        form = Seminar_form()

        Event_data = Seminar.objects.filter(created_by=request.user)
        return render(request, 'staff/seminar/add_seminar.html', {'data':Event_data, 'form':form})
def view_seminar(request):
    pass

def update_seminar(request):
    pass

def delete_seminar(request):
    pass