# Generated by Django 5.0.2 on 2024-03-04 15:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Distance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("distance", models.FloatField()),
                (
                    "from_city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="distances_from",
                        to="chatbot.city",
                    ),
                ),
                (
                    "to_city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="distances_to",
                        to="chatbot.city",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FlightTime",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("flight_time", models.CharField(max_length=50)),
                (
                    "from_city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="flight_times_from",
                        to="chatbot.city",
                    ),
                ),
                (
                    "to_city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="flight_times_to",
                        to="chatbot.city",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TravelPackage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("cost", models.DecimalField(decimal_places=2, max_digits=10)),
                ("destinations", models.ManyToManyField(to="chatbot.city")),
            ],
        ),
    ]