from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Truck

longitude = -80.191_788
latitude = 25.761_681
user_location = Point(longitude, latitude, srid=4326)


class Home(generic.ListView):
    model = Truck
    context_object_name = "trucks"
    queryset = Truck.objects.annotate(
        distance=Distance("location", user_location)
    ).order_by("distance")[0:6]
    template_name = "trucks/index.html"
