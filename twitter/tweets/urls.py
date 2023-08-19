# tweets/urls.py
from django.urls import path
from . import views

app_name = 'tweets'

urlpatterns = [
    path('create/', views.create_tweet, name='create_tweet'),
    # Add more URL patterns as needed
]
