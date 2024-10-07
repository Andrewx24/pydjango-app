import requests
from django.http import JsonResponse
from django.views import View
from bs4 import BeautifulSoup

class ScraperAPI(View):
    def get(self, request):
        # Retrieve scraped data
        data = self.scrape_data()
        return JsonResponse(data)

    def post(self, request):
        # Scrape and store data
        data = self.scrape_data()
        # Here you would typically save the data to your database
        return JsonResponse(data, status=201)  # 201 Created

    def scrape_data(self):
        url = 'https://nextjs-freestyle.vercel.app/apiexample'
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            data = {
                'title': soup.title.string if soup.title else '',
                # Add more fields as needed
            }
            return {'success': True, 'data': data}
        else:
            return {'success': False, 'error': 'Failed to fetch data'}