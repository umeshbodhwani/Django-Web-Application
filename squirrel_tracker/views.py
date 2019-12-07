from django.shortcuts import render

from .models import Squirrel

from django.shortcuts import render, redirect

from django.http import HttpResponse

def main_page(request):
    sq = 'Squirrel Tracker'
    return render(request, 'squirrel_tracker/main.html',{'Squirrel': sq})

def map_get(request):
        sighting = Squirrel.objects.all()[:25]
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
    count_am = 0
    count_pm = 0
    count_running = 0
    count_foraging = 0
    count_approaches = 0
    count_moans = 0
    
    for  item in  Squirrel.objects.all():
       if item.Shift == 'AM':
           count_am += 1
       elif item.Shift == 'PM':
            count_pm += 1
       if item.Running == True:
            count_running += 1
       if item.Foraging == True:
            count_foraging += 1
       if item.Approaches == True:
            count_approaches += 1
       if item.Moans == True:
            count_moans += 1

    context ={
             'AM_count' : count_am,
             'PM_count' : count_pm,
             'Running_count' : count_running,
             'Foraging_count' : count_foraging,
             'Approaches_count' : count_approaches,
             'Moans_count' : count_moans,
        }

    return render(request, 'squirrel_tracker/stat.html', context)
