# views.py

import requests
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        # Print the POST data received
        print("POST Data:", request.POST)

        recipe_title = request.POST.get("title")
        api_url = f'http://127.0.0.1:8000/recipe/{recipe_title}'

        try:
            response = requests.get(api_url)
            print("Response status code:", response.status_code)
            print("Response content:", response.text)

            if response.status_code == 200:
                recipe_data = response.json()
                return render(request, 'result_rec.html', {'recipe_data': recipe_data})
            else:
                return render(request, 'index.html', {'message': 'Failed to fetch recipe details. Check Again!'})

        except requests.exceptions.RequestException as e:
            print("Error:", e)
            return render(request, 'index.html', {'message': 'Failed to fetch recipe details. Check Again!'})

    return render(request, 'index.html')
