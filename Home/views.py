from django.shortcuts import render
from .models import trip,trip_details
import json
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request,"home.html")
def save(request):
    if request.method=="POST":
        data = json.loads(request.body)
        destination=data.get("destination")
        days=data.get("days")
        distance = data.get("distance")
        date = data.get("date")
        transportation = data.get("transportation")
        hotels = data.get("hotels")
        activities = data.get("activities")
        trip_cost = data.get("trip_cost")
        remarks = data.get("remarks")
        visiting_places = data.get("visiting_places")
        fdata = trip(destination=destination)
        fdata.save()
        foreignkey = trip.objects.get(destination=destination)
        appoint_data = trip_details(destination=foreignkey,days=days,distance=distance,date=date,transportation=transportation,hotels=hotels,activities=activities,trip_cost=trip_cost,remarks=remarks,visiting_places=visiting_places)
        appoint_data.save()
        return JsonResponse({"data":"data successfully recieved"})
def initeraries(request):
    data = trip.objects.all()
    return render(request,'itineraries.html',{'context':data})
def fetch_details(request):
    if request.method=="POST":
        data = json.loads(request.body)
        destination = data.get("destination")
        fk = trip.objects.get(destination=destination)
        details = fk.dtrips.first()
        jsondata = json.dumps({'destination':destination,'days':details.days,'distance':details.distance,'date':details.date.isoformat(),'transportation':details.transportation,'hotels':details.hotels,'activities':details.activities,'trip_cost':details.trip_cost,'remarks':details.remarks,'visiting_places':details.visiting_places,})
        return JsonResponse({'data':jsondata})