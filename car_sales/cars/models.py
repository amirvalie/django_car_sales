from django.db import models
from car_sales.common.models import BaseModel
from car_sales.users.models import BaseModel
# Create your models here.



class Car(BaseModel):
    user                 = models.ForeignKey(BaseModel , on_delete=models.PROTECT)
    name                 = models.CharField(max_length=100 , verbose_name='car name')
    colorـname           = models.CharField(max_length=50 , verbose_name='color name')
    number_of_cylinder   = models.PositiveIntegerField(verbose_name='number of cylinder')
    number_of_passangers = models.PositiveIntegerField(vebose_name='number of passangers') 
    
    def __str__(self):
        return car_name