from django.contrib import admin
from django.urls import path, include
from recepies.views import RecipeDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipe/<str:title>/', RecipeDetails.as_view(), name='recipe-details'),
    # Other URL patterns for your project
]
