from django.urls import path
from .views import recommendations_view, recommendation_form  # Make sure you're importing the correct views

urlpatterns = [
    path('form/', recommendation_form, name='recommendation_form'),
    path('api/recommendations/', recommendations_view, name='recommendations_api'),
]

