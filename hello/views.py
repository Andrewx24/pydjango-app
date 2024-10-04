from django.shortcuts import render
from django.http import HttpResponse

from .models import a
def home(request):
    
    return HttpResponse(f"Hello, Django. I am still learning Python and Django!  " + str(a))

def about(request):
    return HttpResponse("About me: I am a Python developer")

def new(request):
    number = request.GET.get('number', '')  # Get the number from the URL query parameter
    return HttpResponse(f"You entered: {number}")