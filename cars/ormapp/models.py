from django.db import models
from django.contrib import admin
class Car_Inventory(models.Model):
    Plate_No= models.CharField(max_length=20,primary_key=True)
    Car_Model=models.CharField(max_length=120)
    Body_Type= models.CharField(max_length=70)
    Mileage= models.IntegerField()
    Engine_Type=models.CharField(max_length=20)
    Make_Date= models.DateField()
    Fuel_Type=models.CharField(max_length=30)
    Horsepower=models.PositiveIntegerField()
    

class Car_InventoryAdmin(admin.ModelAdmin):
     list_display=( 'Plate_No' , 'Car_Model', 'Body_Type', 'Mileage','Engine_Type',
                   'Make_Date','Fuel_Type','Horsepower' )
