import logging
import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os

logger = logging.getLogger(__name__)

# Create your views here.
CROPWIZARD_API_KEY = os.getenv('CROPWIZARD_API')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def chat(request):
    return render(request, 'CropWizard/chat.html')

@csrf_exempt
def ask_cropwizard(request):
    if request.method == 'POST':
        text_data = request.POST.get('text')
        if not text_data:
            return JsonResponse({"error": "No valid input provided."}, status=400)

        url = "https://uiuc.chat/api/chat-api/chat"
        headers = {
            'Content-Type': 'application/json',
        }
        data = {
            "model": "gpt-4",
            "messages": [
                {
                    "role": "system",
                    "content": "Your system prompt here"
                },
                {
                    "role": "user",
                    "content": text_data
                }
            ],
            "openai_key": OPENAI_API_KEY,
            "temperature": 0.1,
            "course_name": "cropwizard-1.5",
            "stream": True,
            "api_key": CROPWIZARD_API_KEY
        }

        response = requests.post(url, headers=headers, json=data)
        return HttpResponse(response.text)

    return HttpResponse(status=405)
