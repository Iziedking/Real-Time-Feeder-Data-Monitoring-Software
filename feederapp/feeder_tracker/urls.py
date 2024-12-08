from django.urls import path, include
from django.conf import settings
from . import views


urlpatterns = [
  path('ibedc_data/', views.fetch_and_update_data, name='fetch_and_update_data'),
  path('', views.test_task, name="test_task")
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls))
    ] + urlpatterns