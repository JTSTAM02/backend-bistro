from django.shortcuts import render
from django.http import JsonResponse
from .models import Menu_Items

def get_menu_items(request):
    menu_items = Menu_Items.objects.all()
    data = []
    for item in menu_items:
        data.append({
            "id": item.id,
            "title": item.title,
            "description": item.description,
            "price": item.price,
            "spicy_level": item.spicy_level,
            "category": {
                "id": item.category_id,
                "name": item.category.name,
            },
            "cuisine": {
            "id": item.cuisine_id,
            "name" : item.category.name,
            }, 
            "location": {
                "id": item.location_id,
                "name": item.location.name,
            }

            })
    return JsonResponse(data, safe=False)
    