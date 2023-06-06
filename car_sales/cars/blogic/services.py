from ..models import Car

def create_car(*,user:str,
        name:str,
        color_name:str,
        number_of_cylinder:int,
        engine_volume:int,
        number_of_passangers:int
    ) -> Car:
    return Car.objects.create(
        name=name,
        color_name=color_name,
        number_of_cylinder=number_of_cylinder,
        engine_volume=engine_volume,
        number_of_passangers=number_of_passangers
    )
 