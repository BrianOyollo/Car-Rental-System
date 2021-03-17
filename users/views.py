from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView, TemplateView, ListView, DetailView, DeleteView, UpdateView
from .models import CustomUser
from ops.models import Vehicle, VehicleProfile, Booking, Agency, Customer
from .forms import CustomerSignUpForm, AgencySignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from ops.forms import BookingForm
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from ops.forms import VehicleUpdateForm, VehicleProfileUpdateForm


# Create your views here.

def register(request):
    return render(request, 'register.html')


def home(request):
    return render(request, 'base.html')


def terms(request):
    return render(request, 'terms.html')


def home(request):
    return render(request, 'base.html')


# def admin(request):
#     return render(request, 'adminDash.html')
# class AdminDashView(LoginRequiredMixin, ListView):
#     model = CustomUser
#     template_name = 'adminDash.html'
#     context_object_name = 'admin'
@login_required()
def admin(request):
    agency_count = Agency.objects.count()
    customer_count = Customer.objects.count()
    cars_count = Vehicle.objects.count()
    bookings = Booking.objects.all()

    return render(request, 'adminDash.html',
                  {'cars_count': cars_count, 'agencies': agency_count, 'customers': customer_count,
                   'bookings': bookings})


class AdminBookingDetailView(DetailView, LoginRequiredMixin):
    model = Booking
    template_name = 'AdminBookingDetailView.html'


class AdminBookingUpdateView(UpdateView, LoginRequiredMixin):
    model = Booking
    form_class = BookingForm
    template_name = 'AdminBookingUpdateView.html'
    success_url = reverse_lazy('admin')


class AdminCustomers(ListView, LoginRequiredMixin):
    model = Customer
    template_name = 'admin_customers.html'
    context_object_name = 'customers'


@require_http_methods(['GET'])
def customer_search(request):
    q = request.GET.get('q')
    error = 'We are sorry. We were not able to find any match'
    if q:
        query = Customer.objects.filter(user__username__icontains=q)
        return render(request, 'customer_search.html', {'query': query})
    return render(request, 'customer_search.html', {'error': error})


class DeleteCustomerView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customers')


class AdminAgencies(ListView, LoginRequiredMixin):
    model = Agency
    template_name = 'admin_agencies.html'
    context_object_name = 'agencies'


@require_http_methods(['GET'])
def agency_search(request):
    q = request.GET.get('q')
    error = 'We are sorry. We were not able to find any match'
    if q:
        query = Agency.objects.filter(user__username__icontains=q)
        return render(request, 'agency_search.html', {'query': query})
    return render(request, 'agency_search.html', {'error': error})


class DeleteAgencyView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('agencies')


class AdminVehiclesView(ListView):
    model = Vehicle
    template_name = 'admin_vehicles.html'
    context_object_name = 'vehicles'


@require_http_methods(['GET'])
def vehicle_search(request):
    q = request.GET.get('q')
    error = 'We are sorry. We were not able to find any match'
    if q:
        query = Vehicle.objects.filter(
            Q(RegNo__icontains=q) | Q(model__icontains=q) | Q(type__icontains=q) | Q(
                owner__user__username__icontains=q))
        return render(request, 'vehicle_search.html', {'query': query})
    return render(request, 'vehicle_search.html', {'error': error})


class DeleteVehicleView(LoginRequiredMixin, DeleteView):
    model = Vehicle
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('vehicles')


@login_required()
def vehicle_profile(self,request,pk):
    vehicle = Vehicle.objects.get(RegNo=self.request.pk)
    if request.method == 'POST':

        v_form = VehicleUpdateForm(request.POST,instance=request.vehicle)
        vp_form = VehicleProfileUpdateForm(request.POST)

        if v_form.is_valid() and vp_form.is_valid():
            v_form.save()
            vp_form.save()

    else:
        v_form = VehicleUpdateForm()
        vp_form = VehicleProfileUpdateForm()

    return render(request, 'vehicle_profile.html', {'v_form': v_form, 'vp_form': vp_form})


@login_required
def agency(request):
    return render(request, 'agencyDash.html')


class CustomerSignup(CreateView):
    model = CustomUser
    form_class = CustomerSignUpForm
    template_name = 'RegisterCustomer.html'
    success_url = reverse_lazy('login')

    # def validation(self, form):
    #     user = form.save()
    #     # login(self.request, user)
    #     return redirect('login')


class AgencySignup(CreateView):
    model = CustomUser
    form_class = AgencySignUpForm
    template_name = 'RegisterAgency.html'
    success_url = reverse_lazy('login')

    # def validation(self, form):
    #     user = form.save()
    #     # login(self.request, user)
    #     return redirect('login')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('admin')
                elif user.is_agency:
                    login(request, user)
                    return redirect('agency')
                else:
                    login(request, user)
                    return redirect('home')
            else:
                messages.warning(request, "Invalid username or password")
        else:
            messages.info(request, "Invalid username or password")
    return render(request, 'login.html', context={'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('home')
