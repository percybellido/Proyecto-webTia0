from django.urls import path
from .views import ResenasCreateView, ResenasListView
app_name="reviews_app" 
urlpatterns = [
           
    path('',ResenasListView.as_view(),name="reviews"),
    path('listar_resenas/',ResenasCreateView.as_view(), name="reviews2"),
    
]