from .selectors import get_car
from ..models import Car
from car_sales.users.models import BaseUser
from car_sales.users.blogic.selectors import get_user
from django.db import transaction
import random
from django.db import IntegrityError


def create_car(
        owner: BaseUser,
        car_name: str,
        car_color: str,
        number_of_cylinder: int,
        engine_volume: int,
        number_of_passengers: int
) -> Car:
    obj = Car.objects.create(
        owner=owner,
        car_name=car_name,
        car_color=car_color,
        number_of_cylinder=number_of_cylinder,
        engine_volume=engine_volume,
        number_of_passengers=number_of_passengers
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
    instances = []
    for i in range(number_of_rows):
        instance = Car(
            owner=user,
            car_name=random.choice(car_names),
            car_color=random.choice(color_names),
            number_of_cylinder=random.randint(1, 20),
            engine_volume=random.randint(1, 50),
            number_of_passengers=random.randint(1, 4),
        )
        instances.append(instance)
    try:
        Car.objects.bulk_create(instances)
        print('====> objects created successfully <====')
    except IntegrityError as ex:
        print(f'Error:{ex}')
