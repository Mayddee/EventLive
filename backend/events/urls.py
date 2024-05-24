from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('events/', views.event_list, name='event_list'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('events/<int:pk>', views.event_detail, name='event_detail'),
    path('book/<int:pk>', views.user_booking, name='user_booking'),
    # path('bookings/', views.user_bookings, name='user_bookings'),
    # path('bookings/<int:pk>', views.user_booking, name='user_booking'),
    path('events/<str:c>', views.event_list_by_category, name='event_list_by_category'),
    path('events/<int:pk>/book/', views.book_event, name='book_event'),
    path('booking/success/', views.booking_success, name='booking_success'),
    path('categories/', views.category_list, name='category_list'),
    
]