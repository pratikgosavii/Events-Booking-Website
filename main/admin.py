from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Event)
admin.site.register(Seminar)
admin.site.register(Lecture)
admin.site.register(Event_Days)
admin.site.register(Event_Prices)
admin.site.register(feedback_questions)