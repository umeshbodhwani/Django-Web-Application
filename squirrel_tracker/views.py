from django.shortcuts import render

from django.shortcuts import render, redirect

from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the squirrel tracker  index.")

def get_map(request):
        sight = Squirrel.objects.all()[:50]
            context ={
                                'sightings' :sight,
                                }
                return render(request, 'squirrel_tracker/map.html',context)
