from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='farm_view_home')
]