from django.forms import SelectDateWidget

from .models import Booking, Vehicle, CustomUser, VehicleProfile
from django import forms
from django.db import transaction
from django.contrib.admin.widgets import AdminDateWidget
from bootstrap_datepicker_plus import DatePickerInput


class DateInput(forms.DateInput):
    input_type = 'date'

    def __init__(self, **kwargs):
        kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['pickup_date', 'return_date', 'pickup_location', 'dropoff_location']
        widgets = {
            'pickup_date': DateInput(),
            'return_date': DateInput(),
        }


class RegisterCar(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

    #
    # @transaction.atomic
    # def save(self):
    #     V=super().save(commit=False)
    #     V.save()
    #     car=VehicleProfile.objects.create(V=V)
    #     car.save()
    #     return V


class VehicleProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = VehicleProfile
        fields = ['best_image', 'image', 'description']


class VehicleUpdateForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['model', 'type', 'seats', 'transmission', 'price']
