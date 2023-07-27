from django.urls import path
from . import views

urlpatterns = [
    path('get_menu_items/', views.get_menu_items, name='get_menu_items'),
]