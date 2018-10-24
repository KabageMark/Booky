from django.db import models
import datetime

# Create your views here.
class Ride(models.Model):
    VEHICLE_CHOICES = (
        ('high', 'high'),
        ('average', 'average'),
        ('low', 'low'),
        
    )
    price = models.IntegerField()
    vehicLe_number = models.CharField(choices=VEHICLE_CHOICES,null=True,max_length=80)
    location = models.CharField(max_length=80)
    

class Book(models.Model):
    LOCATION_CHOICES = (
        ('nakuru', 'nakuru'),
        ('nyeri', 'nyeri'),
        ('mombasa', 'mombasa'),
        
    )  
    price = models.IntegerField()
    location = models.CharField(choices=LOCATION_CHOICES,null=True,max_length=80)
    date_booked = models.DateField(default=datetime.date.today)
     