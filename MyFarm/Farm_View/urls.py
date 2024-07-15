from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='farm_view_home'),
    # path('farm_view/', farm_view, name='farm_view'),
    # path('images/', get_images, name='get_images'),
]