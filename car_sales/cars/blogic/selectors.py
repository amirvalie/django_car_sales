from django.shortcuts import get_object_or_404
from elasticsearch_dsl import Q
from ..models import Car


def get_car(car_id: int) -> Car:
    return get_object_or_404(Car, pk=car_id)


def generate_q_expression(query):
    q=Q(
        'multi_match', query=query,
        fields=[
            'car_name',
            'car_color',
            'owner',
        ], fuzziness='auto')
    return q