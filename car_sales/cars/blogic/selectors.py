from django.shortcuts import get_object_or_404

from ..models import Car


def get_car(car_id: int) -> Car:
    return get_object_or_404(Car, pk=car_id)
