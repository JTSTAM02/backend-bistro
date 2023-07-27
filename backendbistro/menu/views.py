from django.shortcuts import render
from django.http import JsonResponse
from .models import Menu_Items

def get_menu_items(request):
    menu_items = Menu_Items.objects.select_related("category","cuisine").all()
    data = []
    for item in menu_items:
        data.append({
            "id": item.id,
            "title": item.title,
            "description": item.description,
            "price": item.price,
            "spice_level": item.spice_level,
            "category": item.category.name,
            "cuisine": item.category.name, 
            "location": {
                "id": item.location_id,
                "name": item.location.name,
            }

            })
    return JsonResponse(data, safe=False)
    