from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This maps the root URL of 'NewOrleans' to the 'home' view
    # Add other URL patterns for your app here
    path('history/', views.history, name='history'), # This maps the URL of the 'history' view
    path('food/', views.food, name='food'), # This maps the URL of the 'hospitality' view
    path('submit/', views.fun, name='fun'), # This maps the URL of the 'fun' view
    path('thank-you/', views.thank_you, name='thank_you'), # This maps the URL of the 'thankyou' view
    path('retro/', views.retro, name='retro'), # This maps the URL of the 'retrospective' view
    path('details/<int:pk>/', views.details, name='details'), # This maps the URL of the 'details' view
    path('edit/<int:pk>/', views.edit, name='edit'),
]