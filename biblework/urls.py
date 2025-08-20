from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='biblework-home'),
    # Add more URL patterns as needed
]