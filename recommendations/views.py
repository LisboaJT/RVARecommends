from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.conf import settings
import os
import json
from .utils import load_combined_results
from .recommend import get_recommendations  # Adjust the import based on your file structure
from .models import Restaurant


def recommendations_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        favorites = data.get('favorites', [])
        consolidated_file_path = os.path.join(settings.BASE_DIR, 'data', 'combined_results.csv')
        recommended_name = get_recommendations(favorites, consolidated_file_path)[0]
        print(recommended_name)

        # Use the recommended name to fetch additional details from the database
        try:
            restaurant = Restaurant.objects.get(index_name=recommended_name)
            recommendation_details = {
                'name': restaurant.name,
                'description': restaurant.description,
                'address': restaurant.address,
                'phone': restaurant.phone,
                'website': restaurant.website
            }
            print(recommendation_details)
        except Restaurant.DoesNotExist:
            recommendation_details = {}
            print(recommendation_details)

        return JsonResponse({'recommendation': recommendation_details})



def recommendation_form(request):
    # Assuming your Restaurant model has a 'name' field for the restaurant name
    restaurants = Restaurant.objects.filter(is_curated=True)
    options = [{'label': restaurant.name, 'value': restaurant.name} for restaurant in restaurants]
    return render(request, 'recommendations_form.html', {'options': options})


def home(request):
    return HttpResponse('<h1>Welcome to RVA Recommends!</h1><p>Go to <a href="/recommendations/form/">Recommendations Form</a>.</p>')
