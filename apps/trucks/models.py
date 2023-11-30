from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Truck(BaseModel):
    class FacilityChoice(models.TextChoices):
        PUSH_CART = "FR", _("Push Cart")
        TRUCK = "SO", _("Truck")
        UNDEFINED = "JR", _("Undefined")

        @staticmethod
        def from_str(item):
            for value, label in Truck.FacilityChoice.choices:
                if item == label:
                    return value
                return Truck.FacilityChoice.UNDEFINED.value[0]

    class StatusChoice(models.TextChoices):
        REQUESTED = "RQ", _("Truck")
        APPROVED = "AP", _("Push Cart")
        SUSPEND = "SP", _("Suspend")
        EXPIRED = "EX", _("Expired")
        UNDEFINED = "JR", _("Undefined")

        @staticmethod
        def from_str(item):
            for value, label in Truck.StatusChoice.choices:
                if item == label:
                    return value
                return Truck.StatusChoice.UNDEFINED.value[0]

    location_id = models.PositiveIntegerField()
    applicant = models.CharField(max_length=250)
    facility_type = models.CharField(
        max_length=2,
        choices=FacilityChoice.choices,
        default=FacilityChoice.UNDEFINED,
    )
    cnn = models.PositiveIntegerField()
    location_description = models.CharField(max_length=250, blank=True)
    address = models.CharField(max_length=250, blank=True)
    block = models.CharField(max_length=50, blank=True)
    lot = models.CharField(max_length=50, blank=True)
    permit = models.CharField(max_length=50, blank=True)
    status = models.CharField(
        max_length=2, choices=StatusChoice.choices, default=StatusChoice.REQUESTED
    )

    food_items = models.CharField(max_length=450, blank=True)

    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)
    location = models.PointField(null=True, blank=True)
    schedule = models.CharField(max_length=450, blank=True)

    days_hours = models.CharField(max_length=450, blank=True)
    noi_sent = models.CharField(max_length=450, blank=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    received = models.CharField(max_length=450, blank=True)
    prior_permit = models.BooleanField(default=False)
    expiration_date = models.DateTimeField(blank=True, null=True)

    fire_prevention_districts = models.PositiveIntegerField(null=True, blank=True)
    police_districts = models.PositiveIntegerField(null=True, blank=True)
    supervisor_districts = models.PositiveIntegerField(null=True, blank=True)
    zip_codes = models.PositiveIntegerField(null=True, blank=True)
    neighborhoods = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
