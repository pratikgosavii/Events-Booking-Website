from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .models import *
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.urls import reverse
from django.http.response import HttpResponseRedirect

from .forms import *




User = get_user_model()

# Create your views here.


@csrf_exempt
def booking_event(request):
    participants = request.POST.get('name') 
    event_id = request.POST.get('event_id') 

    print(participants)

    event = Event.objects.get(id=event_id)
    event_details = Event.objects.filter(id=event_id)
    
    test = event_ticket_booking.objects.create(owner=request.user, event = event, participants = participants, payment_status = 'Pending')

    if test:

        temp = 'Booking for Event is successful'
        temp1 = ' Event participants names are ' + participants

        temp2 = temp+temp1

        return HttpResponse(temp2)

    else:
        
        return HttpResponse("something went wrong")


def my_bookings(request):

    data = event_ticket_booking.objects.filter(owner=request.user)
    #semianr booking data
    #workshop booking data
    print(data)

    context= {
        'event_data':data,
       
        'event': True,
        'seminar':False,
        'workshop':False,
    }

    return render(request, 'accounts/my-account/my_orders.html', context)




def booking_detail_view(request, booking_id):

    booking_data = event_ticket_booking.objects.get(id = booking_id)
    event_id = booking_data.event.id
    data = Event.objects.get(id = event_id)


    days = Event_Days.objects.filter(event = data)
    schedule = []
    for i in days:
        temp = Day_Schedule.objects.filter(day = i)
        schedule.append(temp)
        print(temp)
        print('-------------------------')

    context= {
        'data':data,
        'days':days,
        'schedule':schedule,
       
    }

    return render(request, 'accounts/my-account/booked_event_view.html', context)


def track_event_booking(request, booking_id):

    a = event_ticket_booking.objects.get(id=booking_id)



    print(a.event.start_date)
    print('---------------------sdsdasdasdsd------------')

    return HttpResponseRedirect(reverse('event_details', kwargs={'event_id':a.event.id}))


def cancle_event_booking(request, booking_id):

    print('jsdbjsbdsbdbsjdsd')
    event_ticket_booking.objects.get(id=booking_id).delete()



    print('Booking cancle')
    return HttpResponseRedirect(reverse('my_bookings'))


def feedback_event(request, event_id):

    if request.method == "POST":

        event_instance = event_ticket_booking.objects.get(id = event_id)
        data =  feedback_questions.objects.filter(event =event_instance.event)


        fed_length = request.POST.get('fed_length')

        print(fed_length)

        kjds = int(fed_length)

        for i in range(kjds):
            st = 'ahahaha' + str(i)
            a = request.POST.get(st)
            print('i')
            print(i)

            print(a)


            z = feedback_answers.objects.create(event = data[0].event, feeback_questions = data[i], user = request.user, stars = a)
        

            print(z)

        return redirect('my_bookings')


    else:

        event_instance = event_ticket_booking.objects.get(id = event_id)

        data =  feedback_questions.objects.filter(event =event_instance.event)

        context= {
            
            'data':data,
            'event_id' : event_id
            
            }

        return render(request, 'accounts/give_feeback.html', context)

