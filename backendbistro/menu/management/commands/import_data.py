import json
import requests
from django.core.management.base import BaseCommand
from menu.models import Category, Cuisine, Location, Menu_Items

class Command(BaseCommand):
    help = 'Imports data from JSON file into the database.'

    def handle(self):
        url = 'https://www.jsonkeeper.com/b/MDXW'
        response = requests.get(url)
        data = response.json()

        for item in data:
            category_name = item.get('category')
            category, _ = Category.objects.get_or_create(name=category_name)
            cuisine_name = item.get('cuisine', 'Default Cuisine')
            cuisine, _ = Cuisine.objects.get_or_create(name=cuisine_name)
            location_name = item.get('location', 'Default Location')
            location, _ = Location.objects.get_or_create(name=location_name)
            spicy_level_value = item.get("spice_level")
            spicy_level_value, _  = spicy_level_value.objects.get_or_create(name=spicy_level_value)
            # try:
            #     spicy_level = int(spicy_level_value)
            # except (ValueError, TypeError):
            #     spicy_level = 0

            menu_item = Menu_Items.objects.create(
                title=item['title'],
                description=item['description'],
                price=item['price'],
                category=category,
                spicy_level=spicy_level_value,
                cuisine=cuisine,
                location=location,
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully added {menu_item}'))