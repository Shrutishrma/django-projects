from django.urls import path
from .views import calculate_interest

urlpatterns = [
    path('', calculate_interest, name='calculate_interest'),
]
