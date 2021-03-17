from django.shortcuts import render, redirect
from .forms import BookingForm, RegisterCar, VehicleUpdateForm, VehicleProfileUpdateForm
from django.contrib import messages
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from .models import Vehicle, VehicleProfile, Booking, Agency, Customer
from .models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db import transaction
from datetime import datetime


# @login_required
# def booking(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             # Booking.customer.id=request.user.id
#             form.instance.customer = request.user
#             vehicle = form.cleaned_data.get('car')
#             if vehicle.is_booked:
#                 messages.warning(request, f"{vehicle.RegNo} is already booked, please pick another vehicle.")
#                 return redirect('fleet')
#             else:
#                 vehicle.is_booked = True
#                 vehicle.save()
#                 form.save()
#                 messages.success(request, f'You have successfully booked {vehicle.RegNo}')
#                 return redirect('home')
#     else:
#         form = BookingForm()
#     return render(request, 'booking1.html', {'form': form})


class RegisterCarView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Vehicle
    fields = ['RegNo', 'model', 'type', 'seats', 'price', 'transmission']
    template_name = 'VehicleRegistration.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # form.instance.owner = self.request.user
        form.instance.owner = Agency.objects.get(user=self.request.user)
        return super().form_valid(form)

    def test_func(self):
        user = self.request.user
        if Agency.objects.filter(pk=user.pk).exists():
            return True


@login_required()
def profile(request):
    if request.method == 'POST':
        v_form = VehicleUpdateForm(request.POST)
        vp_form = VehicleProfileUpdateForm(request.POST)

        if v_form.is_valid() and vp_form.is_valid():
            v_form.save()
            vp_form.save()

    else:
        v_form = VehicleUpdateForm()
        vp_form = VehicleProfileUpdateForm()

    return render(request, 'vehilceprofile.html', {'v_form': v_form, 'vp_form': vp_form})


class FleetView(ListView):
    model = VehicleProfile
    template_name = 'fleet.html'
    context_object_name = 'fleet'


class FleetDetailView(DetailView):
    model = VehicleProfile
    template_name = 'fleet_detail.html'


class BookingView(CreateView):
    model = Booking
    template_name = 'booking1.html'
    # fields = ['pickup_date', 'return_date', 'pickup_location', 'dropoff_location']
    form_class = BookingForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # form.instance.car = Vehicle.objects.get(user=self.request.user)
        # car = Vehicle.objects.get(pk=self.kwargs['pk'])
        # form.instance.car = car.RegNo
        # # form.instance.car_id = Vehicle.objects.get(pk=car)
        # form.instance.customer = Customer.objects.get(user=self.request.user)

        # date1 = form.cleaned_data['pickup_date']
        # date2 = form.cleaned_data['return_date']
        #
        # pickup_date = datetime.strptime(date1, '%d/%m/%Y').date()
        # return_date = datetime.strptime(date2, '%d/%m/%Y').date()
        #
        # form.pickup_date = pickup_date
        # form.return_date = return_date
        form.instance.customer = self.request.user
        car = VehicleProfile.objects.get(pk=self.kwargs['pk'])
        car1 = Vehicle.objects.get(pk=car)
        form.instance.car = car1
        if car1.is_booked:
            messages.warning(self.request, f"{car1.RegNo} is already booked, please pick another vehicle.")
            return redirect('fleet')
        else:
            car1.is_booked = True
            car1.save()
            form.save()
            messages.success(self.request, f'You have successfully booked {car1.RegNo}')
            return redirect('fleet')
        return super().form_valid(form)


def admin_dash_cards(request):
    agency_count = Agency.objects.count()
    customers = Customer.objects.count()
    cars_count = Vehicle.objects.count()

    # context = {
    #     'agencies': agencies,
    #     'customers': customers,
    #     'cars': cars,
    # }
    return render(request, 'adminDash.html', {'cars_count': cars_count, 'agencies': 80})
