from django.contrib import admin
from .models import Vehicle, VehicleProfile, Booking

# Register your models here.
admin.site.register(VehicleProfile)
admin.site.register(Vehicle)
admin.site.register(Booking)