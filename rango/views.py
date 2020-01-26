from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner!")

def a(request):
    return HttpResponse("<h1>This is a test!</h1>")
