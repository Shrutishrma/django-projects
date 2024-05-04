from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeDetails(APIView):
    def get(self, request, title):  # Corrected parameter name from 'Title' to 'title'
        try:
            recipe = Recipe.objects.get(title=title)  # Use lowercase 'title' to match the model field
            serializer = RecipeSerializer(recipe)
            return Response(serializer.data)
        except Recipe.DoesNotExist:
            return Response({"message": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)
