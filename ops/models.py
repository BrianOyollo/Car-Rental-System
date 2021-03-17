
from django.db import models
from multiselectfield import MultiSelectField
from users.models import Customer, CustomUser, Agency
from datetime import datetime


# Create your models here.

carTypes = [
    ('sedan', 'Sedan'),
    ('coupe', 'Coupe'),
    ('suv', 'SUV'),
    ('swagon', 'Station Wagon'),
    ('sports', 'Sports Car'),
    ('convertible', 'Convertible'),
    ('hatchback', 'Hatchback'),
    ('minivan', 'Minivan'),
    ('pickup', 'Pickup Truck'),
    ('bus', 'Bus'),
    ('limo', 'Limousine'),
]
transmission = (
    ('auto', 'Automatic'),
    ('manual', 'Manual'),
)


class Vehicle(models.Model):
    RegNo = models.CharField(primary_key=True, null=False, max_length=10)
    model = models.CharField(null=False, max_length=100)
    type = models.CharField(max_length=15, choices=carTypes, default='sedan')
    owner = models.ForeignKey(Agency, on_delete=models.CASCADE)
    seats = models.CharField(null=False, blank=True, max_length=5)
    transmission = MultiSelectField(choices=transmission)
    price = models.BigIntegerField(blank=False, null=False)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.RegNo}'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class VehicleProfile(models.Model):
    car = models.OneToOneField(Vehicle, on_delete=models.CASCADE, related_name='CarProfile')
    best_image = models.ImageField(upload_to='vehicles', default='no-image1.jpg')
    image = models.ImageField(upload_to='vehicles', default='no-image2.png')
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.car.pk}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Booking(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    car = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    pickup_date = models.DateField(max_length=30)
    return_date = models.DateField(max_length=30)
    pickup_location = models.CharField(max_length=50, default='Agency Location')
    dropoff_location = models.CharField(max_length=50, default='Agency Location')




    def __str__(self):
        return f'{self.customer} {self.car.RegNo} '

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
