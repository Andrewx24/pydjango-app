from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup

from .models import a
def home(request):
    
    return HttpResponse(f"Hello, Django. I am still learning Python and Django!  " + str(a))

def about(request):
   return HttpResponse("About me: I am a Python developer")

def new(request):
    number = request.GET.get('number', '')  # Get the number from the URL query parameter
    return HttpResponse(f"You entered: {number}")

@csrf_exempt
def scrape_and_post(request):
    if request.method in ['GET', 'POST']:
        # Step 1: Scrape the data
        url = 'https://nextjs-freestyle.vercel.app/apiexample'
        response = requests.get(url)
        
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract the data you need
            # This is an example - adjust according to the actual structure of the page
            data = {
                'title': soup.title.string if soup.title else '',
                # Add more fields as needed
            }
            
            # Step 2: Post the data
            # This is where you would typically save the data to your database
            # For this example, we'll just return the scraped data
            return JsonResponse({'success': True, 'data': data})
        else:
            return JsonResponse({'success': False, 'error': 'Failed to fetch data'}, status=400)
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)