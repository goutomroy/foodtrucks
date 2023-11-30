from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from apps.trucks.models import Truck


@admin.register(Truck)
class TruckAdmin(OSMGeoAdmin):
    list_display = (
        "location_id",
        "applicant",
        "location_description",
        "location",
    )
    list_filter = (
        "status",
        "days_hours",
    )
