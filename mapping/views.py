from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from . import models


# Load AdminArea Data
def adminAreajson(request):
    adminArea = serialize('geojson', models.AdminArea.objects.all())
    return HttpResponse(adminArea)


# Load Boundary Data
def boundaryjson(request):
    boundary = serialize('geojson', models.Boundary.objects.all())
    return HttpResponse(boundary)


# Load Street Data
def streetjson(request):
    street = serialize('geojson', models.Street.objects.all())
    return HttpResponse(street)


# Load Amenity Data
def amenityjson(request):
    amenity = serialize('geojson', models.Amenity.objects.all())
    return HttpResponse(amenity)


# Load Bicycle Data
def bicyclejson(request):
    bicycle = serialize('geojson', models.Bicycle.objects.all())
    return HttpResponse(bicycle)


# Load Bridge Data
def bridgejson(request):
    bridge = serialize('geojson', models.Bridge.objects.all())
    return HttpResponse(bridge)


# Load Building Data
def buildingjson(request):
    building = serialize('geojson', models.Building.objects.all())
    return HttpResponse(building)


# Load Cycleway Data
def cyclewayjson(request):
    cycleway = serialize('geojson', models.Cycleway.objects.all())
    return HttpResponse(cycleway)


# Load Embassy Data
def embassyjson(request):
    embassy = serialize('geojson', models.Embassy.objects.all())
    return HttpResponse(embassy)



# Load Emergency Data
def emergencyjson(request):
    emergency = serialize('geojson', models.Emergency.objects.all())
    return HttpResponse(emergency)


# Load Golf Data
def golfjson(request):
    golf = serialize('geojson', models.Golf.objects.all())
    return HttpResponse(golf)



# Load Government Data
def governmentjson(request):
    government = serialize('geojson', models.Government.objects.all())
    return HttpResponse(government)


# Load Highway Data
def highwayjson(request):
    highway = serialize('geojson', models.Highway.objects.all())
    return HttpResponse(highway)



# Load Industrial Data
def industrialjson(request):
    industrial = serialize('geojson', models.Industrial.objects.all())
    return HttpResponse(industrial)


# Load Landuse Data
def landusejson(request):
    landuse = serialize('geojson', models.Landuse.objects.all())
    return HttpResponse(landuse)


# Load Names Data
def namesjson(request):
    names = serialize('geojson', models.Names.objects.all())
    return HttpResponse(names)


# Load Natural Data
def naturaljson(request):
    natural = serialize('geojson', models.Natural.objects.all())
    return HttpResponse(natural)



class Dashboard(TemplateView):
    template_name = 'dashboard.html'