from django.urls import path
from .views import RegisterCarView, FleetView, FleetDetailView, BookingView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('fleet/<pk>/', FleetDetailView.as_view(), name='fleet-detail'),
    path('fleet/<pk>/book/', BookingView.as_view(), name='booking'),
    path('fleet/', FleetView.as_view(), name='fleet'),
    # path('profile/',vehicleprofile.as_view(), name='profile'),
    path('VehicleRegistration/', RegisterCarView.as_view(), name='vehicle-registration'),
]
