# Back-End Bistro (API Creation)

## MoSCoW

    - Must-Haves:
        *  Store data in the PostgreSQL datbase
            * "Menu Items" table must include:
                - Title
                - Description
                - Price
                - Spice Level
                - Foreign Key to Category Table
                -Foreign Key to Cuisine

            * "Category" table must include:
                - Appetizers
                - Desserts
                - Main Dish

            * "Cuisine" table must contain:
                - American
                - Thai
                - Chinese

        * Connect to React Restaurant App as API

    - Should-Haves: 
        * diagram to display the table schema

    - Could-Haves:
        * different location table with primary key and foreign key in menu items table

    - Won't Have:
        * Class Based Views or Decorators


## Questions
    - Do I have to define Id for each table or does it auto increment and create that?
    - How to Join data together from foreign and primary keys? (category, cuisine, location)
    - Cuisine and Category classes are identical. How could I combine them for DRY code?


## Models (class based structure for the tables)
    1. Create class for each Table
    
    from django.db import models

    class MenuItems(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField()
        price = models.DecimalField(max_digits=8)
        spicy_level = models.IntegerField()
        category = models.ForeignKey(CASCADE?)
        cuisine = models.ForeignKey(CASCADE?)
        location = models.ForeignKey(CASCADE?)

        def __str__(self):
            return self.title

    class Cuisine(models.Model):
        type = models.CharField(max_length = 100)

        def __str__(self):
            return self.type


    class Category(models.Model):
        type = models.CharField(max_length = 100)

        def __str__(self):
            return self.type


    class Locations(models.Model):
        name = models.CharField(max_length=200)

        def __str__(self):
            return self.name

## Views (actual Python functions to be implemented)

from django.http import JsonResponse

    - def get_menu_items(request)
        menu_items = MenuItem.object.all()
        data = []
        for item in menu_items:
            data.append({
                "id": item.id,
                "title": item.title,
                "description": item.description,
                "price": item.price,
                "spice_level": item.spice_level,
                "category": item.category_id,
                "cuisine": item.cuisine_id,
                "location": locations_id,

            })



## EndPoints
    - /menu_items
    - /breakfast
    - /lunch
    - /dinner
    - /appetizers


## Database Schema/Table Relationships

    - I want four tables
        * Menu_items
        * Category
        * Cuisine
        * Locations

    - Each table has specific columns (see MoSCoW)
    - see (https://dbdiagram.io/d/64c15c9802bd1c4a5ebffe5e)

    ![diagram] (/Users/tylerstamm/Desktop/Database Diagram-Backend Bistro.png)


        
