from django.urls import path
from hello import views
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path('about/', views.about, name='about'),
    path('new/', views.new, name='new'),
    path('scrape-and-post/', views.scrape_and_post, name='scrape-and-post'),
]

