"""
URL configuration for railway_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from railway.views import (
    RegisterView, LoginView, LogoutView, TrainViewSet, 
    BookTicketView, MyBookingsView, CancelBookingView,
    list_trains, get_train
)

# Router for TrainViewSet (handles /trains/)
router = DefaultRouter()
router.register(r'trains', TrainViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),                 # Django Admin Panel
    path('api/register/', RegisterView.as_view(), name='register'),  # User Registration
    path('api/login/', LoginView.as_view(), name='login'),           # User Login
    path('api/logout/', LogoutView.as_view(), name='logout'),        # User Logout
    path('api/book/', BookTicketView.as_view(), name='book_ticket'), # Book Train Ticket
    path('api/my-bookings/', MyBookingsView.as_view(), name='my_bookings'), # User Bookings
    path('api/cancel-booking/<int:booking_id>/', CancelBookingView.as_view(), name='cancel_booking'), # Cancel Booking
    path('api/list-trains/', list_trains, name='list_trains'),       # List all trains
    path('api/train/<int:train_id>/', get_train, name='get_train'),  # Retrieve a specific train
    path('api/', include(router.urls)),  # Includes TrainViewSet routes (CRUD operations for trains)
]
