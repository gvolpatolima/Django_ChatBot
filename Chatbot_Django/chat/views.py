from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is my first url")

def specific(request):
    return HttpResponse("asdasd")