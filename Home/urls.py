from django.urls import path
from Home import views

urlpatterns=[
    path('',views.home,name='home'),
    path('saveplan',views.save,name="saveplan"),
    path('myitineraries',views.initeraries,name="itineraries"),
    path('fetchdetails',views.fetch_details,name="fetch_details"),
]