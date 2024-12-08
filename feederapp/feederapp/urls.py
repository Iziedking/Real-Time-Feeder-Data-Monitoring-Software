
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('feeder_tracker.urls')),
    path('admin/', admin.site.urls),
]
