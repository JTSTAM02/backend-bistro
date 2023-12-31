from django.db import models


#------------------------------Category Class---------------------------------------------------
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#-------------------------------Cuisine Class---------------------------------------------------
class Cuisine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


#-------------------------------Locations Class---------------------------------------------------
class Location(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


#------------------------------Menu_Items Class---------------------------------------------------
class Menu_Items(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    spice_level = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cuisine_type = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

