from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


from django.conf import settings
User = settings.AUTH_USER_MODEL




# Create your models here.
class feedback(models.Model):
    owner =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='asdsd')
    description = models.CharField(max_length=555)


class Report(models.Model):
    owner =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='adsdsd')
    description = models.CharField(max_length=555)

  