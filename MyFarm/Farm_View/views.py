from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

from django.shortcuts import render
import requests
import datetime

import logging

logger = logging.getLogger(__name__)

def home(request):
    image_api_url = 'http://127.0.0.1:5000/images/Seventh%20Leaf/2024-07-08/farmy-1/images/top_right/left/20240708-115006.jpg'

    try:
        # Fetch image data from API
        response = requests.get(image_api_url)
        response.raise_for_status()  # Raise exception for 4xx/5xx errors

        # Get the image URL from the response (assuming JSON response)
        image_data = response.json()
        image_url = image_data['url']


        # Pass the image URL to the template for rendering
        return render(request, 'Farm_View/farm_view.html', {'image_url': image_url})

    except requests.exceptions.RequestException as e:
        # Handle request exceptions (e.g., network errors)
        # return render(request, 'Farm_View/farm_view.html', {'error': str(e)})
        return None

    # return render(request, 'Farm_View/farm_view.html')

# def home(request):
#     image_api_url = "http://127.0.0.1:5000/images/Seventh Leaf/2024-07-08/farmy-1/images/top_right/left/20240708-115006.jpg"

#     try:
#         # Fetch image data from API
#         response = requests.get(image_api_url)
#         response.raise_for_status()  # Raise exception for 4xx/5xx errors

#         # Assuming JSON response containing the image URL
#         image_data = response.json()
#         image_url = image_data['url']
#         print("Image Url: ", image_url)

#         # Pass the image URL to the template for rendering
#         return render(request, 'Farm_View/farm_view.html', {'image_url': image_url})

#     except requests.exceptions.RequestException as e:
#         # Handle request exceptions (e.g., network errors)
#         # return render(request, 'Farm_View/farm_view.html', {'error': str(e)})
#         return None

# def farm_view(request):
#     image_api_url = "http://127.0.0.1:5000/images/Seventh%20Leaf/2024-07-08/farmy-1/images/top_right/left/20240708-115006.jpg"
#     time_date  = datetime.datetime()
#     try:
#         # Fetch image data from API
#         response = requests.get(image_api_url)
#         response.raise_for_status()  # Raise exception for 4xx/5xx errors

#         # Assuming JSON response containing the image URL
#         image_data = response.json()
#         image_url = image_data['url']
#         print("Image Url: ", image_url)

#         # Pass the image URL to the template for rendering
#         return render(request, 'Farm_View/farm_view.html', {'image_url': image_url}, {"time_date":time_date})

#     except requests.exceptions.RequestException as e:
#         # Handle request exceptions (e.g., network errors)
#         return render(request, 'Farm_View/farm_view.html', {'error': str(e)})

# def get_images(request):
#     date = request.GET.get('date', datetime.today().strftime('%Y-%m-%d'))
#     parts = request.GET.getlist('part')

#     images = []

#     if 'rgb_center' in parts:
#         images.append('/path/to/rgb_center_image_' + date + '.jpg')
#     if 'infrared_left' in parts:
#         images.append('/path/to/infrared_left_image_' + date + '.jpg')
#     if 'infrared_right' in parts:
#         images.append('/path/to/infrared_right_image_' + date + '.jpg')
#     if 'live_feed' in parts:
#         images.append('/path/to/live_feed_image_' + date + '.jpg')

#     print(request)

#     return JsonResponse(images, safe=False)
    # return None

# def fetch_image(request):
#     # Example URL of the image API
#     image_api_url = '127.0.0.1:5000/images'

#     try:
#         # Fetch image data from API
#         response = requests.get(image_api_url)
#         response.raise_for_status()  # Raise exception for 4xx/5xx errors

#         # Get the image URL from the response (assuming JSON response)
#         image_data = response.json()
#         image_url = image_data['url']

#         # Pass the image URL to the template for rendering
#         return render(request, 'app/fetch_image.html', {'image_url': image_url})

#     except requests.exceptions.RequestException as e:
#         # Handle request exceptions (e.g., network errors)
#         return render(request, 'app/fetch_image.html', {'error': str(e)})