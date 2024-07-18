from django.shortcuts import render

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