from django.urls import path

from dashboard.views import *

urlpatterns = [

    #event add delete
    path('', index, name='index'),
    path('staff/', staff_dashbaord, name='staff_dashbaord'),
    path('staff/show-event/', show_event, name='show_event'),
    path('staff/add-event/', add_event, name='add_event'),
    path('staff/details-event/<event_id>', view_event, name='view_event'),
    path('staff/update-event/<event_id>', update_event, name='update_event'),
    path('staff/delete-event/<event_id>', delete_event, name='delete_event'),

    path('staff/add-form/<event_id>', add_form, name='add_form'),
    path('staff/update-event/<event_id>', update_event, name='wrefefe'),

    path('staff/show-event-winner/', show_event_winner, name='show_event_winner'),
    path('staff/add-event-winner/', add_event_winner, name='add_event_winner'),
    path('staff/update-event-winner/<event_id>', update_event_winner, name='update_event_winner'),
    path('staff/delete-event-winner/<_id>', delete_event_winner, name='delete_event_winner'),

    
    
    #event days
    path('staff/event/days_show/<event_id>/', show_days, name='show_days'),
    path('staff/event/day-add/<event_id>/', add_day, name='add_day'),
    path('staff/event/details-day/<day_id>/', view_details_day, name='detail_days'),
    path('staff/event/day-update/<day_id>/', update_day, name='update_day'),
    path('staff/event/delete-day/<event_id>/', delete_day, name='delete_day'),

    #day schedule
    path('staff/event/show-day-schedule/<day_id>', show_day_schedule, name='show_day_schedule'),
    path('staff/event/add_day_schedule_form/<day_id>', add_day_schedule_form, name='add_day_schedule_form'),
    path('staff/event/add-day-schedule/<day_id>', add_day_schedule, name='add_day_schedule'),
    path('staff/event/day-schedule-details/<day_schedule_id>', view_day_schedule, name='day_schedule_details'),
    path('staff/event/day-schedule-update/<day_schedule_id>', update_day_schedule, name='day_schedule_update'),
    path('staff/event/day-schedule-delete/<day_schedule_id>', day_schedule_delete, name='day_schedule_delete'),

    path('staff/event/generate_qr/<event_id>', generate_gr, name='generate_gr'),

    
    #seminars urls
    path('staff/list-seminars/', show_seminars, name='ds'),
    path('staff/add-seminar/', add_seminars, name='add_seminar'),
    path('staff/details-seminar/<seminar_id>', view_seminar, name='s'),
    path('staff/update-semianr/<seminar_id>', update_seminar, name='sds'),
    path('staff/delete-seminar/<seminar_id>', delete_seminar, name='d'),

]