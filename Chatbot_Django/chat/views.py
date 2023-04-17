from django.shortcuts import render
from django.http import HttpResponse

import openai

def index(request):
    return render(request, 'chat/index.html')

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    return HttpResponse(userMessage)
