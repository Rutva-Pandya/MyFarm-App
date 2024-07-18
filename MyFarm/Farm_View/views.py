from django.shortcuts import render

def home(request):
    # List of image URLs
    urls = [
        "https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg",
        "https://images.pexels.com/photos/3573357/pexels-photo-3573357.jpeg",
        # Add more URLs as needed
    ]
    
    return render(request, 'farm_view.html', {'urls': urls})

# from django.shortcuts import render
# from django.http import JsonResponse
# from datetime import datetime

# from django.shortcuts import render
# import requests
# import datetime

# import logging

# logger = logging.getLogger(__name__)

# # def home(request):
# #     image_api_url = 'http://127.0.0.1:5000/images/Seventh%20Leaf/2024-07-08/farmy-1/images/top_right/left/20240708-115006.jpg'

# #     try:
# #         # # Fetch image data from API
# #         # response = requests.get(image_api_url)
# #         # response.raise_for_status()  # Raise exception for 4xx/5xx errors

# #         # # Get the image URL from the response (assuming JSON response)
# #         # image_data = response.json()
# #         # image_url = image_data.get('url', '')  # Ensure 'url' key exists

# #         # print("Image URL:", image_url)  # Debug print
# #         image_url = 'https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg'

# #         # Pass the image URL to the template for rendering
# #         return render(request, 'Farm_View/farm_view.html', {'image_url': image_url})

# #     except requests.exceptions.RequestException as e:
# #         # Handle request exceptions (e.g., network errors)
# #         return render(request, 'Farm_View/farm_view.html', {'error': str(e)})


# # from django.shortcuts import render 

# def home(request):
#     # Specific image URL for testing
#     url = ['https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg']

#     # Pass the image URL to the template for rendering
#     return render(request, 'MyFarm/Farm_View/templates/Farm_View/farm_view.html', {'url': url})


# # def home(request):
# #     image_api_url = 'http://127.0.0.1:5000/images/Seventh%20Leaf/2024-07-08/farmy-1/images/top_right/left/20240708-115006.jpg'

# #     try:
# #         # Fetch image data from API
# #         response = requests.get(image_api_url)
# #         response.raise_for_status()  # Raise exception for 4xx/5xx errors

# #         # Get the image URL from the response (assuming JSON response)
# #         image_data = response.json()
# #         image_url = image_data['url']

# #         print(image_url)

# #         # Pass the image URL to the template for rendering
# #         return render(request, 'Farm_View/farm_view.html', {'image_url': image_url})

# #     except requests.exceptions.RequestException as e:
# #         # Handle request exceptions (e.g., network errors)
# #         return render(request, 'Farm_View/farm_view.html', {'error': str(e)})
# #         # return None

