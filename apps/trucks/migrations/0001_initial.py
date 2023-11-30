# Generated by Django 4.2.7 on 2023-11-30 11:24

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Truck",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("location_id", models.PositiveIntegerField()),
                ("applicant", models.CharField(max_length=250)),
                (
                    "facility_type",
                    models.CharField(
                        choices=[
                            ("FR", "Push Cart"),
                            ("SO", "Truck"),
                            ("JR", "Undefined"),
                        ],
                        default="JR",
                        max_length=2,
                    ),
                ),
                ("cnn", models.PositiveIntegerField()),
                ("location_description", models.CharField(blank=True, max_length=250)),
                ("address", models.CharField(blank=True, max_length=250)),
                ("block", models.CharField(blank=True, max_length=50)),
                ("lot", models.CharField(blank=True, max_length=50)),
                ("permit", models.CharField(blank=True, max_length=50)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("RQ", "Truck"),
                            ("AP", "Push Cart"),
                            ("SP", "Suspend"),
                            ("EX", "Expired"),
                            ("JR", "Undefined"),
                        ],
                        default="RQ",
                        max_length=2,
                    ),
                ),
                ("food_items", models.CharField(blank=True, max_length=450)),
                ("x", models.FloatField(blank=True, null=True)),
                ("y", models.FloatField(blank=True, null=True)),
                (
                    "location",
                    django.contrib.gis.db.models.fields.PointField(
                        blank=True, null=True, srid=4326
                    ),
                ),
                ("schedule", models.CharField(blank=True, max_length=450)),
                ("days_hours", models.CharField(blank=True, max_length=450)),
                ("noi_sent", models.CharField(blank=True, max_length=450)),
                ("approved_date", models.DateTimeField(blank=True, null=True)),
                ("received", models.CharField(blank=True, max_length=450)),
                ("prior_permit", models.BooleanField(default=False)),
                ("expiration_date", models.DateTimeField(blank=True, null=True)),
                (
                    "fire_prevention_districts",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                (
                    "police_districts",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                (
                    "supervisor_districts",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                ("zip_codes", models.PositiveIntegerField(blank=True, null=True)),
                ("neighborhoods", models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
