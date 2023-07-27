from django.http import JsonResponse
from .models import Menu_Items

def get_menu_items(request):
    # use 'select_related' to get 'category' and 'cuisine' data
    menu_items = Menu_Items.objects.select_related("category","cuisine").all()
    data = []
    for item in menu_items:
        data.append({ # creates dictionary that has menu items attributes
            "id": item.id, # realized too late I didn't need this
            "title": item.title,
            "description": item.description,
            "price": item.price,
            "spice_level": item.spice_level,
            "category": item.category.name,
            "cuisine": item.cuisine.name, 
            "location": {
                "id": item.location_id,
                "name": item.location.name,
            }

            })
        # JsonResponse turns data into JSON
        # 'safe=False' needed because data parameter is a list, not a dictionary
    return JsonResponse(data, safe=False)
    