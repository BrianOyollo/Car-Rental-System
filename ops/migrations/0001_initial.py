# Generated by Django 3.0.7 on 2021-02-24 03:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('RegNo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('sedan', 'Sedan'), ('coupe', 'Coupe'), ('suv', 'SUV'), ('swagon', 'Station Wagon'), ('sports', 'Sports Car'), ('convertible', 'Convertible'), ('hatchback', 'Hatchback'), ('minivan', 'Minivan'), ('pickup', 'Pickup Truck'), ('bus', 'Bus'), ('limo', 'Limousine')], default='sedan', max_length=15)),
                ('seats', models.CharField(blank=True, max_length=5)),
                ('transmission', multiselectfield.db.fields.MultiSelectField(choices=[('auto', 'Automatic'), ('manual', 'Manual')], max_length=11)),
                ('price', models.BigIntegerField()),
                ('is_booked', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Agency')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best_image', models.ImageField(default='defaultcar.jpg', upload_to='vehicles')),
                ('image', models.ImageField(default='defaultcar.jpg', upload_to='vehicles')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='CarProfile', to='ops.Vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_date', models.DateTimeField(default=datetime.datetime.now, max_length=8)),
                ('return_date', models.DateTimeField(max_length=8)),
                ('pickup_location', models.CharField(default='Agency Location', max_length=50)),
                ('dropoff_location', models.CharField(default='Agency Location', max_length=50)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ops.Vehicle')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
