from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('api/admin-area/', views.adminAreajson, name='adminareajson'),
    path('api/boundaryjson/', views.boundaryjson, name='boundaryjson'),
    path('api/streetjson/', views.streetjson, name='streetjson'),
    path('api/amenityjson/', views.amenityjson, name='amenityjson'),
    path('api/bicyclejson/', views.bicyclejson, name='bicyclejson'),
    path('api/bridgejson/', views.bridgejson, name='bridgejson'),
    path('api/buildingjson/', views.buildingjson, name='buildingjson'),
    path('api/cyclewayjson/', views.cyclewayjson, name='cyclewayjson'),
    path('api/embassyjson/', views.embassyjson, name='embassyjson'),
    path('api/emergencyjson/', views.emergencyjson, name='emergencyjson'),
    path('api/golfjson/', views.golfjson, name='golfjson'),
    path('api/governmentjson/', views.governmentjson, name='governmentjson'),
    path('api/highwayjson/', views.highwayjson, name='highwayjson'),
    path('api/industrialjson/', views.industrialjson, name='industrialjson'),
    path('api/landusejson/', views.landusejson, name='landusejson'),
    path('api/namesjson', views.namesjson, name='namesjson'),
    path('api/naturaljson', views.naturaljson, name='naturaljson'),
]