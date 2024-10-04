from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path('about/', views.about, name='about'),
    path('new/', views.new, name='new'),
]

