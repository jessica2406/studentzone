from django.db import models

# Create your models here.
class Event(models.Model):
    Event_name=models.CharField(max_length=100)
    Event_Description=models.TextField()
    Event_Venue=models.CharField(max_length=100)
    Event_start_date_time = models.DateTimeField()
    Event_end_date_time = models.DateTimeField()
    Event_Image=models.ImageField()