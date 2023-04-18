from django.shortcuts import render
from django.http import HttpResponse

import openai
from . import env
import random

def index(request):
    return render(request, 'chat/index.html')


def getResponse(request):
    openai.api_key = env.API_KEY

    userMessage = request.GET.get('userMessage')
    prompt = f"User: {userMessage}\nAI:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        temperature=random.uniform(0.5, 1),
        n=1,
        stop=None,
    )

    aiMessage = response.choices[0].text.strip()
    return HttpResponse(aiMessage)
