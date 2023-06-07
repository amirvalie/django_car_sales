from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from .models import Car
from .blogic.services import create_car
from .permissions import IsInSalesGroup
from car_sales.api.mixins import ApiAuthMixin


class CreateCarApi(ApiAuthMixin, APIView):
    permission_classes = [IsAuthenticated, IsInSalesGroup]

    class InputCarSerializer(serializers.Serializer):
        car_name = serializers.CharField(max_length=255)
        car_color = serializers.CharField(max_length=50)
        number_of_cylinder = serializers.IntegerField(min_value=1)
        engine_volume = serializers.IntegerField(min_value=624)
        number_of_passangers = serializers.IntegerField(min_value=1)

    class OutputCarSerializer(serializers.ModelSerializer):
        user = serializers.ReadOnlyField(source='user.email')

        class Meta:
            model = Car
            fields = (
                'user',
                'car_name',
                'car_color',
                'number_of_cylinder',
                'engine_volume',
                'number_of_passangers',
            )

    @extend_schema(request=InputCarSerializer, responses=OutputCarSerializer)
    def post(self, request):
        serializer = self.InputCarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            car = create_car(
                user=request.user,
                car_name=serializer.validated_data['car_name'],
                car_color=serializer.validated_data['car_color'],
                number_of_cylinder=serializer.validated_data['number_of_cylinder'],
                engine_volume=serializer.validated_data['engine_volume'],
                number_of_passangers=serializer.validated_data['number_of_passangers'],
            )
        except Exception as ex:
            return Response(
                f'Database error {ex}'
            )
        return Response(self.OutputCarSerializer(car).data)
