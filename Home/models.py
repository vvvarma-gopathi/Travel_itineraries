from django.db import models

# Create your models here.
class trip(models.Model):
    destination = models.CharField(max_length=125,primary_key=True)
class trip_details(models.Model):
    destination = models.ForeignKey(trip,related_name='dtrips',on_delete=models.CASCADE)
    days = models.IntegerField(null=False)
    distance = models.IntegerField(null=False)
    date = models.DateField(null=False)
    transportation = models.CharField(max_length=10,null=False)
    hotels = models.CharField(max_length=200)
    activities = models.CharField(max_length=300,null=False)
    trip_cost = models.IntegerField(null=False)
    remarks = models.CharField(max_length=600)
    visiting_places = models.CharField(max_length=300)