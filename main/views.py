from django.http import JsonResponse
from django.shortcuts import redirect, render

from booking.models import feedback_answers
from .models import *
from .forms import *
from datetime import datetime

# Create your views here.

from django.contrib.auth.decorators import user_passes_test


def staff_required(login_url=None):
    return user_passes_test(lambda u: u.is_staff, login_url=login_url)


def events(request):

    data = Event.objects.all()
    return render(request, 'events_show.html', {'data':data})

def event_details(request, event_id):

    data = Event.objects.get(id = event_id)
    days = Event_Days.objects.filter(event = data)
    schedule = []
   

    for i in days:
        temp = Day_Schedule.objects.filter(day = i)
        schedule.append(temp)
       
    print(schedule)
    print(days[0].start_date)


    return render(request, 'event_detail_view.html', {'data':data, 'days':days, 'schedule':schedule})



def seminars(request):

    data = Seminar.objects.all()
    return render(request, 'seminars_show.html', {'data':data})

def lectures(request):

    data = Lecture.objects.all()
    return render(request, 'lectures_show.html', {'data':data})


def event_winners(request):
    
    data = Event_Prices.objects.all()

    return render(request, 'event_winners.html', {'data':data})




def add_feedback_questions(request, event_id):

    if request.method == "POST":

        print('here')


        fe_questions = request.POST.getlist('fe_questions[]')
        # event_id = request.POST.get('event_id')

        print(event_id)

        event_id = Event.objects.get(id = event_id)

        for i in fe_questions:

            feedback_questions.objects.create(event = event_id, fed_questions = i)

        
        return JsonResponse({'status':'done'})


    else:

        form = feedback_questions_Form()

        return render(request, 'staff/event/add_feedback_questions.html', {'form' : form, 'event_id' : event_id})


def list_feedback_questions(request, event_id):

   
    a = Event.objects.get(id = event_id)


    b = feedback_questions.objects.filter(event = a)

    print(b.count())

    star = []
    co = 0

    for i in b:
        
        fed_data = feedback_answers.objects.filter(feeback_questions = i)
        print('in questions answeer')
        print(fed_data.count())
        for z in fed_data:

            co = co + z.stars
        if co > 0:
            star.append(co/len(fed_data))
        else:
            star.append('0')

        co = 0


    return render(request, 'staff/event/list_feedback_questions.html', {'data' : b, 'event' : a})



def update_feedback_questions(request, feeback_id):


    if request.method == "POST":


        instance = feedback_questions.objects.get(id = feeback_id)

        data = request.POST.get('dynamic')

        instance.fed_questions = data
        instance.save()

        return redirect('list_feedback_questions', event_id = instance.event.id)


    else:

        instance = feedback_questions.objects.get(id = feeback_id)


        return render(request, 'staff/event/update_feedback_questions.html', {'instance' : instance})




def delete_feedback_questions(request, feeback_id):

    instance = feedback_questions.objects.get(id = feeback_id)
    instance_id = instance.event.id
    instance.delete()

    return redirect('list_feedback_questions', event_id = instance_id )