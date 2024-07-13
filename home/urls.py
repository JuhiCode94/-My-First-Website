from django.contrib import admin
from django.urls import path
from home import views

# Define URL patterns to map URLs to their corresponding view functions
urlpatterns = [
    # Home page
    path("", views.index, name='home'),
    # About page
    path("about", views.about, name='about'),
    # Cake page
    path("cake", views.cake, name='cake'),
    # Chocolate page
    path("chocolate", views.chocolate, name='chocolate'),
    # Ice cream page
    path("icecream", views.icecream, name='icecream'),
    # Privacy page
    path("privacy", views.privacy, name='privacy'),
    # Privacy page
    path("terms", views.terms, name='terms'),
    # Contact page
    path("contact", views.contact, name='contact'),
    # Order confirmation page
    path("order_confirmation", views.order_confirmation, name='order_confirmation'),
    # Order summary page
    path('order_summary/', views.order_summary, name='order_summary'),
    # Subscription page
    path('subscribe/', views.subscribe, name='subscribe'),
    # Search results page
    path('search_results/', views.search_results, name='search_results'),  # Add this line
]