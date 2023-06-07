from django.db import models
from car_sales.common.models import BaseModel
from car_sales.users.models import BaseUser

# Create your models here.

class Car(models.Model):
    user = models.ForeignKey(BaseUser, on_delete=models.PROTECT)
    car_name = models.CharField(max_length=250, verbose_name='car name')
    car_color = models.CharField(max_length=50, verbose_name='car color name')
    number_of_cylinder = models.PositiveIntegerField(verbose_name='number of cylinder')
    engine_volume = models.PositiveIntegerField(verbose_name='engine volume')
    number_of_passangers= models.PositiveIntegerField(verbose_name='number of passangers')

    def __str__(self):
        return self.car_name