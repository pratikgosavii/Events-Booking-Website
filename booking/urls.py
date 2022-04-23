from django.urls import path

from  .views import *

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #urls for parents/student
    path('event/', booking_event, name='booking_event'),
    
    path('track-event-booking/<booking_id>', track_event_booking, name='track_event_booking'),

    path('feedback-event/<event_id>', feedback_event, name='feedback_event'),

    path('cancle-event-booking/<booking_id>', cancle_event_booking, name='cancle_event_booking'),

    path('my-bookings/', my_bookings, name='my_bookings'),

    path('booking-detail-view/<booking_id>', booking_detail_view, name='booking_detail_view'),

    
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)