from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is my first url")

def specific(request):
    numre = 55
    return HttpResponse("numre")

def article(request, particle_id):
    return HttpResponse(particle_id)