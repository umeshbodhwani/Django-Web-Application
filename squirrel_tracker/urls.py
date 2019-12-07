#This file is for inserting all the URL's of Squirrel Tracker

from django.urls import path

from . import views

app_name = 'squirrel_tracker'

urlpatterns = [

    path('',views.main_page, name= 'main'),
    path('map', views.map_get, name='map'),
    path('sightings/',views.sighting_get, name='sighting'),
    path('sightings/<str:Unique_squirrel_ID>/',views.edit_sq, name = 'edit_sighting'),
    path('sightings/add',views.add_sq, name = 'add_sighting'),
    path('sightings/stats', views.stats, name = 'stats'),
    
    ]
