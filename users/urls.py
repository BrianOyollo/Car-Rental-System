from django.urls import path
from . import views
from .views import admin, AdminBookingDetailView, AdminBookingUpdateView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin, name='admin'),
    path('admin/<pk>/bookingdetails/', AdminBookingDetailView.as_view(), name='booking-details'),
    path('admin/<pk>/updatebookingdetails/', AdminBookingUpdateView.as_view(), name='update-booking-details'),
    path('admin/customers/', views.AdminCustomers.as_view(), name='customers'),
    path('admin/vehicles/', views.AdminVehiclesView.as_view(), name='vehicles'),
    path('admin/vehicles/search/', views.vehicle_search, name='vehicle-search-results'),
    path('admin/customers/search/', views.customer_search, name='customer-search-results'),
    path('admin/agencies/', views.AdminAgencies.as_view(), name='agencies'),
    path('admin/agencies/search/', views.agency_search, name='agency-search-results'),
    path('admin/customers/<pk>/delete/', views.DeleteCustomerView.as_view(), name='delete-customer'),
    path('admin/agencies/<pk>/delete/', views.DeleteAgencyView.as_view(), name='delete-agency'),
    path('admin/vehicles/<pk>/delete/', views.DeleteVehicleView.as_view(), name='delete-vehicle'),
    path('admin/vehicles/<pk>/profile/', views.vehicle_profile, name='vehicle-profile'),
    path('home/', views.home, name='home'),
    path('agency/', views.agency, name='agency'),
    path('CustomerSignup/', views.CustomerSignup.as_view(), name='customer-signup'),
    path('AgencySignup/', views.AgencySignup.as_view(), name='agency-signup'),
]
