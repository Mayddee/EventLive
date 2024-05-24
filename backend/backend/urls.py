
from django.contrib import admin
from django.urls import path, include
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    # path('events/', include('events.urls')),
    path('api/', include('events.urls'))
]
