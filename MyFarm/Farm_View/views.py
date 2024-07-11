from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def home(request):
    return render(request, 'Farm_View/farm_view.html')

def farm_view(request):
    return render(request, 'Farm_View/farm_view.html')

def get_images(request):
    date = request.GET.get('date', datetime.today().strftime('%Y-%m-%d'))
    parts = request.GET.getlist('part')

    images = []

    if 'rgb_center' in parts:
        images.append('/path/to/rgb_center_image_' + date + '.jpg')
    if 'infrared_left' in parts:
        images.append('/path/to/infrared_left_image_' + date + '.jpg')
    if 'infrared_right' in parts:
        images.append('/path/to/infrared_right_image_' + date + '.jpg')
    if 'live_feed' in parts:
        images.append('/path/to/live_feed_image_' + date + '.jpg')

    return JsonResponse(images, safe=False)