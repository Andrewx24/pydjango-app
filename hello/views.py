from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django. I am  still still learning Python and Django!")


def about(request):
    return HttpResponse("About me: I am a Python")

