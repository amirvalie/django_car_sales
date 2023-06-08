from .selectors import get_car
from ..models import Car
from car_sales.users.models import BaseUser
from car_sales.users.selectors import get_user
from django.db import transaction
import random
from django.db import IntegrityError


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


@transaction.atomic
def update_car(
        car_id: int,
        **kwargs
) -> Car:
    car_obj = get_car(car_id=car_id)
    for field, value in kwargs.items():
        setattr(car_obj, field, value)
    car_obj.save()
    return car_obj


def create_bulk_car(number_of_rows: int) -> None:
    user = get_user(pk=1)
    car_names = [
        "Toyota Corolla",
        "Honda Civic",
        "Ford Mustang",
        "Chevrolet Camaro",
        "Tesla Model S",
        "Nissan Altima",
        "BMW 3 Series",
        "Mercedes-Benz C-Class",
        "Audi A4",
        "Jeep Wrangler",
        "Subaru Impreza",
        "Mazda MX-5 Miata",
        "Porsche 911",
        "Lamborghini Huracan",
        "Ferrari 488 GTB",
        "McLaren 720S",
        "Bugatti Chiron",
        "Koenigsegg Agera RS",
        "Pagani Huayra",
        "Rolls-Royce Phantom"
    ]
    color_names = [
        "Red",
        "Blue",
        "Green",
        "Yellow",
        "Orange",
        "Purple",
        "Black",
        "White",
        "Gray",
        "Silver",
        "Gold",
        "Brown",
        "Beige",
        "Pink",
        "Turquoise",
        "Magenta",
        "Cyan",
        "Olive",
        "Navy",
        "Maroon"
    ]
    number_of_cylinder = [2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]
    engine_volumes = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6,
                      4.8]
    number_of_passangers = [2, 4]
    instances = []
    for i in range(number_of_rows):
        instance = Car(
            user=user,
            car_name=random.choice(car_names),
            car_color=random.choice(color_names),
            number_of_cylinder=random.choice(number_of_cylinder),
            engine_volume=random.choice(engine_volumes),
            number_of_passangers=random.choice(number_of_passangers),
        )
        instances.append(instance)
    try:
        Car.objects.bulk_create(instances)
        print('====> objects created successfully <====')
    except IntegrityError as ex:
        print(f'Error:{ex}')
