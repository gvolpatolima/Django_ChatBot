from django.shortcuts import render
from django.http import HttpResponse

import openai
from . import env

def index(request):
    return render(request, 'chat/index.html')


# last_user_input = ""
#
# def getResponse(request):
#     global last_user_input
#     openai.api_key = env.API_KEY
#
#     userMessage = request.GET.get('userMessage')
#     if userMessage == last_user_input:
#         aiMessage = "I'm sorry, I didn't understand that."
#     else:
#         last_user_input = userMessage
#         prompt = f"User: {userMessage}\nAI:"
#
#         response = openai.Completion.create(
#             engine="ada",
#             prompt=prompt,
#             max_tokens=50,
#             temperature=0.5,
#             n=1,
#         )
#
#         aiMessage = response.choices[0].text.strip()
#
#     return HttpResponse(aiMessage)


def getResponse(request):
    openai.api_key = env.API_KEY

    userMessage = request.GET.get('userMessage')
    prompt = f"User: {userMessage}\nAI:"

    response = openai.Completion.create(
        engine="ada",
        prompt=prompt,
        max_tokens=50,
        temperature=0.5,
        n=1,
    )

    aiMessage = response.choices[0].text.strip()
    return HttpResponse(aiMessage)
