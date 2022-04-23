from django.urls import path

from accounts import views

urlpatterns = [
    #urls for parents/student
    path('student/login/', views.student_login_view, name='student_login_view'),
    path('student/signup/', views.student_signup_view, name='student_signup_view'),
    path('student/logout/', views.student_signup_view, name='logout'),
    
    path('booking_detail_view/<booking_id>', views.booking_detail_view, name='booking_detail_view'),

    path('my_bookings/', views.my_bookings, name='my_bookings'),
    # path('my_bookings/', views.my_bookings, name='my_bookings'),
    
]