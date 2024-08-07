import logging
import requests
from openai import AzureOpenAI 
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os

logger = logging.getLogger(__name__)

# Create your views here.
CROPWIZARD_API_KEY = "uc_5806ac979cae4911a920231ca15abad7"

def chat(request):
    return render(request, 'CropWizard/chat.html')

@csrf_exempt
def ask_cropwizard(request):
    if request.method == 'POST':
        text_input = request.POST.get('text', '')
        image_url_input = request.POST.get('image_url', '')

        if not text_input and not image_url_input:
            return JsonResponse({"error": "No valid input provided."}, status=400)

        # url = "https://uiuc-chat-git-refactortoopenaimessagefix-kastandays-projects.vercel.app/api/chat-api/chat"
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

        if image_url_input:
            messages.append({
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url_input
                        }
                    }
                ]
            })

        if text_input:
            if image_url_input:
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
            "model": "gpt-4o",
            "messages": messages,
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
