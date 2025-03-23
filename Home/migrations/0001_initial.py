# Generated by Django 5.1.7 on 2025-03-23 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trip',
            fields=[
                ('destination', models.CharField(max_length=125, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='trip_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.IntegerField()),
                ('distance', models.IntegerField()),
                ('date', models.DateField()),
                ('transportation', models.CharField(max_length=10)),
                ('hotels', models.CharField(max_length=200)),
                ('activities', models.CharField(max_length=300)),
                ('trip_cost', models.IntegerField()),
                ('remarks', models.CharField(max_length=600)),
                ('visiting_places', models.CharField(max_length=300)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dtrips', to='Home.trip')),
            ],
        ),
    ]
