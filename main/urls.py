from django.urls import path

from  .views import *

urlpatterns = [
    #urls for parents/student
    path('events', events, name='events'),
    path('seminars', seminars, name='seminars'),

    path('add_feedback_questions/<event_id>', add_feedback_questions, name='add_feedback_questions'),
    path('list_feedback_questions/<event_id>', list_feedback_questions, name='list_feedback_questions'),
    path('update_feedback_questions/<feeback_id>', update_feedback_questions, name='update_feedback_questions'),
    path('delete_feedback_questions/<feeback_id>', delete_feedback_questions, name='delete_feedback_questions'),
    
    path('event-details/<event_id>', event_details, name='event_details'),
    path('event-winners', event_winners, name='event_winners'),
    path('seminars', seminars, name='seminar'),
    path('lectures', lectures, name='lecture'),
    
    path('seminars-details/<event_id>', seminars_details, name='seminars_details'),
    path('event-winners', event_winners, name='event_winners'),
    path('seminars', seminars, name='seminar'),
    path('lectures', lectures, name='lecture'),
    
]