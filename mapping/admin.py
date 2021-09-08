from django.contrib import admin
from . import models
from leaflet.admin import LeafletGeoAdmin



@admin.register(models.AdminArea)
class AdminAreaAdmin(LeafletGeoAdmin):
    list_display = ['full_id', 'name_en', 'admin_leve']


@admin.register(models.Boundary)
class BoundaryAdmin(LeafletGeoAdmin):
    list_display = ['full_id', 'name_en', 'boundary']


@admin.register(models.Street)
class StreetAdmin(LeafletGeoAdmin):
    list_display = ['full_id', 'name_en']


@admin.register(models.Amenity)
class AmenityAdmin(LeafletGeoAdmin):
    list_display = ['full_id', 'name_en']



@admin.register(models.Bicycle)
class BicycleAdmin(LeafletGeoAdmin):
    list_display = ['full_id', 'name_en']



@admin.register(models.Bridge)
class BridgeAdmin(LeafletGeoAdmin):
    list_display = ['full_id', 'name_en']



@admin.register(models.Building)
class BuildingAdmin(LeafletGeoAdmin):
    list_display = ['full_id', 'name_en']



@admin.register(models.Cycleway)
class CyclewayAdmin(LeafletGeoAdmin):
    list_display = ['full_id', 'cycleway']



@admin.register(models.Embassy)
class EmbassyAdmin(LeafletGeoAdmin):
    list_display = ['full_id', 'name_en']



@admin.register(models.Emergency)
class EmergencyAdmin(LeafletGeoAdmin):
    list_display = ['full_id', 'name_en']



@admin.register(models.Golf)
class GolfAdmin(LeafletGeoAdmin):
    list_display = ['full_id', 'name_en']



@admin.register(models.Government)
class GovernmentAdmin(LeafletGeoAdmin):
    list_display = ['full_id', 'name_en']


@admin.register(models.Highway)
class HighwayAdmin(LeafletGeoAdmin):
    list_display = ['full_id', 'name_en']



@admin.register(models.Industrial)
class IndustrialAdmin(LeafletGeoAdmin):
    list_display = ['full_id', 'name']


@admin.register(models.Landuse)
class LanduseAdmin(LeafletGeoAdmin):
    list_display = ['full_id', 'name_en']



@admin.register(models.Names)
class NamesAdmin(LeafletGeoAdmin):
    list_display = ['full_id', 'name']


@admin.register(models.Natural)
class NaturalAdmin(LeafletGeoAdmin):
    list_display = ['full_id', 'name_en']


