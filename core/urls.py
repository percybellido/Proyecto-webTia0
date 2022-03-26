from django.urls import path

from . import views
    
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    
    path('request_a_quote/', views.request_a_quote, name="request_a_quote"),
    path('deals/', views.deals, name="deals"),
       
]