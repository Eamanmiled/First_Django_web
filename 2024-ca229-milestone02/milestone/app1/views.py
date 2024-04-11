from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.shortcuts import get_object_or_404

def index(request):
    areas = Area.objects.all()
    return render(request, 'index.html', {'areas':areas})

def areas(request):
    areas = Area.objects.all()
    return render(request, 'areas.html', {'areas':areas})

def attractions(request):
    attr = Attraction.objects.all()
    return render(request, 'attractions.html', {'attractions': attr})

def single_area(request, id):
    target = get_object_or_404(Area, id=id)
    return render(request, 'singleArea.html', {'area': target})