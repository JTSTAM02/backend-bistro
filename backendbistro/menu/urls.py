from django.views import get_menu_items
from django.urls import path

urlpatterns = [
    path('menu_items/', get_menu_items, name='menu_items'),
]