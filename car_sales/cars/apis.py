from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from .models import Car
from .blogic.services import create_car, update_car
from .blogic.selectors import generate_q_expression
from .permissions import IsInSalesGroup
from car_sales.api.mixins import ApiAuthMixin
from rest_framework import status
from car_sales.search.documents import CarDocument
from rest_framework.pagination import LimitOffsetPagination
from elasticsearch_dsl import Q


class CreateCarApi(ApiAuthMixin, APIView):
    permission_classes = [IsAuthenticated, IsInSalesGroup]

    class InputCarSerializer(serializers.Serializer):
        car_name = serializers.CharField(max_length=255)
        car_color = serializers.CharField(max_length=50)
        number_of_cylinder = serializers.IntegerField(min_value=1)
        engine_volume = serializers.FloatField(min_value=1.0)
        number_of_passengers = serializers.IntegerField(min_value=1)

    class OutputCarSerializer(serializers.ModelSerializer):
        owner = serializers.ReadOnlyField(source='owner.email')

        class Meta:
            model = Car
            fields = (
                'owner',
                'car_name',
                'car_color',
                'number_of_cylinder',
                'engine_volume',
                'number_of_passengers',
            )

    @extend_schema(request=InputCarSerializer, responses=OutputCarSerializer)
    def post(self, request):
        serializer = self.InputCarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            car = create_car(
                owner=request.user,
                car_name=serializer.validated_data['car_name'],
                car_color=serializer.validated_data['car_color'],
                number_of_cylinder=serializer.validated_data['number_of_cylinder'],
                engine_volume=serializer.validated_data['engine_volume'],
                number_of_passengers=serializer.validated_data['number_of_passengers'],
            )
        except Exception as ex:
            return Response(
                f'Database error {ex}'
            )
        return Response(self.OutputCarSerializer(car).data, status=status.HTTP_201_CREATED)


class UpdateCarApi(ApiAuthMixin, APIView):
    permission_classes = [IsAuthenticated, IsInSalesGroup]

    class InputCarSerializerPut(serializers.Serializer):
        car_name = serializers.CharField(max_length=255, required=False)
        car_color = serializers.CharField(max_length=50, required=False)
        number_of_cylinder = serializers.IntegerField(min_value=1, required=False)
        engine_volume = serializers.IntegerField(min_value=624, required=False)
        number_of_passengers = serializers.IntegerField(min_value=1, required=False)

    class OutputCarSerializerPut(serializers.ModelSerializer):
        owner = serializers.ReadOnlyField(source='owner.email')

        class Meta:
            model = Car
            fields = (
                'owner',
                'car_name',
                'car_color',
                'number_of_cylinder',
                'engine_volume',
                'number_of_passengers',
            )

    @extend_schema(request=InputCarSerializerPut, responses=OutputCarSerializerPut)
    def put(self, request, car_id):
        serializer = self.InputCarSerializerPut(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            car = update_car(
                car_id=car_id,
                **serializer.validated_data
            )
        except Exception as ex:
            return Response(
                f'Database error {ex}',
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(self.OutputCarSerializerPut(car).data,status=status.HTTP_200_OK)


class CarSearchAPIView(ApiAuthMixin,APIView, LimitOffsetPagination):
    document_class = CarDocument
    class OutputCarSerializer(serializers.ModelSerializer):
        owner = serializers.ReadOnlyField(source='owner.email')
        class Meta:
            model = Car
            fields = (
                'owner',
                'car_name',
                'car_color',
                'number_of_cylinder',
                'engine_volume',
                'number_of_passengers',
            )

    def get(self, request, query):
        try:
            q = generate_q_expression(query)
            search = CarDocument.search().query(q)
            response = search.execute()
            results = self.paginate_queryset(response, request, view=self)
            serializer = self.OutputCarSerializer(response, many=True)
            return self.get_paginated_response(serializer.data)
        except BaseException as ex: 
            return Response(
                f'Erro {ex}',
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )