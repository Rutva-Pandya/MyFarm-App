from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat, name='chat'),
    path('ask_cropwizard/', views.ask_cropwizard, name='ask_cropwizard'),
]
