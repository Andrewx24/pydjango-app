from django.urls import path, re_path
from hello import views
from . import views
from .api import ScraperAPI

from django.views.generic import TemplateView

urlpatterns = [
    path("", views.home, name="home"),
    path('about/', views.about, name='about'),
    path('new/', views.new, name='new'),
    path('scrape-and-post/', views.scrape_and_post, name='scrape-and-post'),
    path('api/scraper/', ScraperAPI.as_view(), name='api-scrape'),
     re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]

