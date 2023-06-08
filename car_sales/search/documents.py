from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from car_sales.cars.models import Car


@registry.register_document
class CarDocument(Document):
    owner = fields.ObjectField(properties={
        'email':fields.TextField(),
    })
    class Index:
        name = 'carsdocument'

    class Django:
        model = Car
        fields = [
            'id',
            'car_name',
            'car_color',
            'number_of_cylinder',
            'engine_volume',
            'number_of_passengers',
        ]