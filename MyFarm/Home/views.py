import os
from django.shortcuts import render
from openai import AzureOpenAI

OPENAI_API_KEY = os.getenv('AZURE_OPENAI_API_KEY')
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version= "2023-12-01-preview",
    azure_endpoint = "https://gpt-4-uiuc-chat-east-us-2.openai.azure.com/"
)

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def sensor_data(request):
    return render(request, 'sensorData.html')

def satellite_images(request):
    return render(request, 'satelliteImages.html')

def farm_images(request):
    return render(request, 'Farm_View/farm_view.html')

def crop_wizard(request):
    return render(request, 'CropWizard/chat.html')