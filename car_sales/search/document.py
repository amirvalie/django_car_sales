from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from car_sales.cars.models import Car


@registry.register_document
class CarDocument(Document):
    user = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'email': fields.TextField(),
    })

    class Index:
        name = 'cars'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Car
        fields = [
            'id',
            'car_name',
            'car_color',
            'number_of_cylinder',
            'engine_volume',
            'number_of_passangers',
        ]
