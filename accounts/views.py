from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.urls import reverse
from booking.models import *
from django.contrib.auth.decorators import login_required



User = get_user_model()
# Create your views here.


def student_login_view(request):

    if request.method == "POST":
        print('1')
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)

        if email !=  None or password != None:
            print('2')
            user=authenticate(request, email=email, password=password)
            print('printing user')
            print(user)
            if user is not None:
                print('3')
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print("something went wrong1")
                return HttpResponseRedirect(reverse('student_login_view'))
        else:
            print("something went wrong2")
            return HttpResponseRedirect(reverse('view-product'))
    else:
        print('4')
        return render(request, 'accounts/login.html')

def student_signup_view(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print('----------------')
        print(email)
        print(password1)
        print(password2)
       

        if email != None or password1 != None or password2 != None:

            if password1 == password2:
                print('1')
            
            
                user=authenticate(email=email, password=password1)

                if user is not None:
                    
                    print('user alrweady exsist')
                    return render(request, 'accounts/signup.html')

                    
                else:
                    print('2')

                    account1 = User.objects.create_user(email=email, password=password1)
                    account1.save()
                    if account1:
                        return HttpResponseRedirect(reverse('student_login_view'))
                    else:
                        print('something went wrong')
                        return render(request, 'accounts/signup.html')

            else:
                print('password is not same')
                return render(request, 'accounts/signup.html')
                

        else:
            print('3')

            return render(request, 'accounts/signup.html')

    else:

        print('4')

        return render(request, 'accounts/signup.html')

@login_required(login_url="http://127.0.0.1:8000/accounts/student/login/") 
def my_bookings(request):

    data = event_ticket_booking.objects.filter(owner=request.user)
    print(data)

    return render(request, 'accounts/my_bookings.html', {'event_data':data})


def booking_detail_view(request, booking_id):
    

    data = event_ticket_booking.objects.get(id=booking_id, owner = request.user)
    print('--------------------')
    print(data.event.image)


    return render(request, 'accounts/my_event_detail_view.html', {'data':data})
