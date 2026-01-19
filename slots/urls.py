"""
URL Configuration for Slots App
"""
from django.urls import path
from . import views

app_name = 'slots'

urlpatterns = [
    # Authentication URLs
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Main functionality URLs
    path('dashboard/', views.dashboard, name='dashboard'),
    path('book/<int:slot_id>/', views.book_slot, name='book_slot'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('booking-history/', views.booking_history, name='booking_history'),
]
