from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sensorData/', views.sensor_data, name='sensor_data'),
    path('satelliteImages/', views.satellite_images, name='satellite_images'),
    path('farmImages/', views.farm_images, name='farm_images'),
    path('cropWizard/', views.crop_wizard, name='crop_wizard'),
]
