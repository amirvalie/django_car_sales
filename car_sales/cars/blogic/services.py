from ..models import Car
from car_sales.users.models import BaseUser


def create_car(
        user: BaseUser,
        car_name: str,
        car_color: str,
        number_of_cylinder: int,
        engine_volume: int,
        number_of_passangers: int
) -> Car:
    obj = Car.objects.create(
        user=user,
        car_name=car_name,
        car_color=car_color,
        number_of_cylinder=number_of_cylinder,
        engine_volume=engine_volume,
        number_of_passangers=number_of_passangers
    )
    return obj
