from django.shortcuts import render

from .models import Squirrel

from django.shortcuts import render, redirect

from django.http import HttpResponse

from .forms import SquirrelForm

def main_page(request):

     sq = 'Squirrel Tracker'
     context = {'Squirrel':sq
            }
     return render(request, 'squirrel_tracker/main.html',context)

def map_get(request):
        sighting = Squirrel.objects.all()[:100]
        context ={
                'sightings' :sighting,
                                }
        return render(request, 'squirrel_tracker/map.html',context)

def sighting_get(request):
    sqs = Squirrel.objects.all()
    context = {
            'squirrels': sqs,
        }
    return render(request, 'squirrel_tracker/sighting.html',context)

def edit_sq(request, Unique_squirrel_ID):
    squirrel = Squirrel.objects.get(Unique_squirrel_ID = Unique_squirrel_ID)
    if request.method == "POST":
        form= SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SquirrelForm(instance= squirrel)
        context ={
            'form':form
        }

        return render(request,'squirrel_tracker/edit.html',context)

def add_sq(request):
    if request.method == "POST":
        form= SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
        else:
            form = SquirrelForm()
        context ={
            'form':form,
        }
        return render(request,'squirrel_tracker/edit.html',context)

def stats(request):

        
    sq_count = len(Squirrel.objects.all())
    count_am = len(Squirrel.objects.filter(Shift = 'AM'))
    count_pm = len(Squirrel.objects.filter(Shift = 'PM'))
    climbing_count = len( Squirrel.objects.filter(Climbing = True))
    cin_color = len(Squirrel.objects.filter(Primary_Fur_Color= 'Cinnamon'))
    black_color = len(Squirrel.objects.filter(Primary_Fur_Color= 'Black'))
    count_moans = len( Squirrel.objects.filter(Moans = True))
    count_running = len( Squirrel.objects.filter(Running = True))
    count_foraging = len(Squirrel.objects.filter(Foraging = True))
    count_approaches = len(Squirrel.objects.filter(Approaches = True))
    eating_count = len( Squirrel.objects.filter(Eating = True))

    context ={
             'squirrel_count':sq_count,
             'AM_count' : count_am,
             'PM_count' : count_pm,
             'Climbing_count': climbing_count,
             'Eating_count': eating_count,
             'Running_count' : count_running,
             'Foraging_count' : count_foraging,
             'Approaches_count' : count_approaches,
             'Moans_count' : count_moans,
             'Cinnamon_color': cin_color,
             'Black_color' : black_color
        }

    return render(request, 'squirrel_tracker/stat.html', context)
