import logging
import requests
from openai import AzureOpenAI
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os

logger = logging.getLogger(__name__)

# Create your views here.
CROPWIZARD_API_KEY = os.getenv('CROPWIZARD_API')
OPENAI_API_KEY = os.getenv('AZURE_OPENAI_API_KEY')
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version= "2023-12-01-preview",
    azure_endpoint = "https://gpt-4-uiuc-chat-east-us-2.openai.azure.com/"
)

def chat(request):
    return render(request, 'CropWizard/chat.html')

@csrf_exempt
def ask_cropwizard(request):
    if request.method == 'POST':
        text_input = request.POST.get('text', '')
        image_url_input = request.POST.get('image_url', '')

        # Handle image file upload
        image_file = request.FILES.get('image')

        if not text_input and not image_url_input and not image_file:
            return JsonResponse({"error": "No valid input provided."}, status=400)

        # Save the uploaded image if it exists
        image_url = ''
        if image_file:
            image_path = os.path.join(settings.MEDIA_ROOT, image_file.name)
            with open(image_path, 'wb') as f:
                for chunk in image_file.chunks():
                    f.write(chunk)
            image_url = os.path.join(settings.MEDIA_URL, image_file.name)

        url = "https://uiuc.chat/api/chat-api/chat"
        headers = {
            'Content-Type': 'application/json'
        }

        messages = [
            {
                "role": "system",
                "content": "Your system prompt here"
            }
        ]

        if image_url:
            messages.append({
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url
                        }
                    }
                ]
            })

        if text_input:
            if image_url:
                messages[-1]["content"].append({
                    "type": "text",
                    "text": text_input
                })
            else:
                messages.append({
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": text_input
                        }
                    ]
                })

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": messages,
            "openai_key": OPENAI_API_KEY,
            "temperature": 0.1,
            "course_name": "cropwizard-1.5",
            "stream": False,
            "api_key": CROPWIZARD_API_KEY
        }

        response = requests.post(url, headers=headers, json=payload)
        response_data = response.json()

        if 'message' in response_data:
            return JsonResponse(response_data)
        else:
            return JsonResponse({"error": "Invalid response from API."}, status=500)

    return HttpResponse(status=405)
