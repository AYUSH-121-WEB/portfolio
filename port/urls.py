
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.home, name='index'),
    path('about', views.about, name='about'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contact', views.contact, name='contact'),
    
]
