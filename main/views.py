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




def add_feedback_questions(request):

    if request.method == "POST":

        print('here')


        fe_questions = request.POST.getlist('fe_questions[]')
        event_id = request.POST.get('event_id')

        print(event_id)

        event_id = Event.objects.get(id = event_id)

        for i in fe_questions:

            feedback_questions.objects.create(event = event_id, fed_questions = i)

        
        return JsonResponse({'status':'done'})


    else:

        form = feedback_questions_Form()
        event_values = Event.objects.filter(created_by = request.user)

        return render(request, 'staff/event/add_feedback_questions.html', {'form' : form, 'event_values' : event_values})


def list_feedback_questions(request):

    print(request.user)

    a = Event.objects.filter(created_by = request.user)

    print(a.count())
    print('in event')


    for y in a:

        print('in questions')
        b = feedback_questions.objects.filter(event = y)

        print(b.count())

        star = []
        co = 0

        for i in b:
            
            fed_data = feedback_answers.objects.filter(feeback_questions = i)
            print('in questions answeer')
            print(fed_data.count())
            for z in fed_data:

                co = co + z.stars

            star.append(co/len(fed_data))

            co = 0


      

    print('pritning staar')

    print(star)



        

    return render(request, 'staff/event/list_feedback_questions.html', {'data' : a})



def update_feedback_questions(request, feeback_id):


    if request.method == "POST":


        instance = feedback_questions.objects.get(id = feeback_id)

        data = request.POST.get('dynamic')

        instance.fed_questions = data
        instance.save()

        return redirect('list_feedback_questions')


    else:

        instance = feedback_questions.objects.get(id = feeback_id)


        return render(request, 'staff/event/update_feedback_questions.html', {'instance' : instance})




def delete_feedback_questions(request, feeback_id):

    feedback_questions.objects.get(id = feeback_id).delete()

    return redirect(list_feedback_questions)