from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^(?P<vehicle_id>\d+)/$', views.click_vehicle, name='click_vehicle'),
    url(r'^$', views.vehicle_display, name = 'vehicle_display'),
    url(r'^add_vehicle/$', views.add_vehicle, name='add_vehicle'),
    url(r'^save_vehicle/$', views.save_vehicle, name='save_vehicle'),
]

