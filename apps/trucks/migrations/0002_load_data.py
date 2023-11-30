# Generated by Django 4.2.7 on 2023-11-29 23:06
import csv
from pathlib import Path

from django.contrib.gis.geos import fromstr
from django.db import migrations
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.utils.timezone import make_aware

from apps.trucks.models import Truck

DATA_FILENAME = "initial_data/food_truck_data.csv"


def read_file_generator():
    csv_file = Path(__file__).parent.parent / DATA_FILENAME
    with open(csv_file, mode="r") as file:
        lines = csv.DictReader(file)
        for line in lines:
            yield line


def load_data(apps, schema_editor):

    """
    TODO: commented fields need to recheck, as well as for fields
    """

    objs = read_file_generator()
    for obj in objs:
        try:
            location_id = obj.get("locationid")
            applicant = obj.get("Applicant")
            facility_type = Truck.FacilityChoice.from_str(obj.get("FacilityType"))
            cnn = obj.get("cnn")
            location_description = obj.get("LocationDescription")
            address = obj.get("Address")
            block = obj.get("block")
            lot = obj.get("lot")

            permit = obj.get("permit")
            status = Truck.FacilityChoice.from_str(obj.get("Status"))
            food_items = obj.get("FoodItems")
            # x = obj.get("X")
            # y = obj.get("Y")

            latitude = obj.get("Latitude")
            longitude = obj.get("Longitude")
            location = fromstr(f"POINT({longitude} {latitude})", srid=4326)

            schedule = obj.get("Schedule")

            days_hours = obj.get("dayshours")
            noi_sent = obj.get("NOISent")

            # in_format = "%m/%d/%Y %H:%M:%S %p"
            # to_format = "%Y-%m-%d %H:%M:%S %p"
            #
            #
            # approved_date = obj.get("Approved")
            #
            # if approved_date:
            #     approved_date = timezone.datetime.strptime(
            #         approved_date, in_format
            #     ).strftime(to_format)
            #     approved_date = parse_date(approved_date)

            received = obj.get("Received")
            prior_permit = obj.get("PriorPermit")

            # expiration_date = obj.get("ExpirationDate")
            # if expiration_date:
            #     expiration_date = timezone.datetime.strptime(
            #         expiration_date, in_format
            #     ).strftime(to_format)
            #     expiration_date = parse_date(expiration_date)

            fire_prevention_districts = obj.get("Fire Prevention Districts")
            police_districts = obj.get("Police Districts")
            supervisor_districts = obj.get("Supervisor Districts")
            zip_codes = obj.get("Zip Codes")
            neighborhoods = obj.get("Neighborhoods")

            Truck(
                location_id=location_id,
                applicant=applicant,
                facility_type=facility_type,
                cnn=cnn,
                location_description=location_description,
                address=address,
                block=block,
                lot=lot,
                permit=permit,
                status=status,
                food_items=food_items,
                # x=x,
                # y=y,
                location=location,
                schedule=schedule,
                days_hours=days_hours,
                noi_sent=noi_sent,
                # approved_date=approved_date,
                received=received,
                prior_permit=prior_permit,
                # expiration_date=expiration_date,
                # fire_prevention_districts=fire_prevention_districts,
                # police_districts=police_districts,
                # supervisor_districts=supervisor_districts,
                # zip_codes=zip_codes,
                neighborhoods=neighborhoods,
            ).save()
        except KeyError:
            pass


class Migration(migrations.Migration):
    dependencies = [
        ("trucks", "0001_initial"),
    ]

    operations = [migrations.RunPython(load_data)]
