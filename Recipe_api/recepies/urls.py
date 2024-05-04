from django.urls import path
from .views import RecipeDetails

urlpatterns = [
    path('recipe/<str:title>/', RecipeDetails.as_view(), name='recipe-details'),
    # Other URL patterns for different views if needed
]
