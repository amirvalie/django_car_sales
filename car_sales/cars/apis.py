from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from .models import Car
from .blogic.services import create_car

class CarApi(APIView):
    def InputCarSerializer(serializers.Serializer):
        name                 = serializers.CharField(max_length=255)
        colorـname           = serializers.CharField(max_length=50)
        number_of_cylinder   = serializers.IntegerField(min_value=1)
        engine_volume        = serializers.IntegerField(min_value=624)
        number_of_passangers = serializers.IntegerField(min_value=1)
    
    def OutputCarSerializer(serializer.ModelSerializer):
        user = serializers.ReadOnlyField(source='user.email')
        class Meta:
            model  = Car
            fields = (
                'user',
                'name',
                'color_name',
                'number_of_cylinder',
                'engine_volume',
                'number_of_passangers',
            )

    def post(self,request):
        serializer=self.InputCarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            car = create_car(
                user = request.user
                name = serializer.validated_data['name'],
                color_name = serializer.validated_data['color_name'],
                number_of_cylinder = serializer.validated_data['number_of_cylinder'],
                engine_volume = serializer.validated_data['engine_volume'],
                number_of_passangers = serializer.validated_data['number_of_passangers'],
            )
        except Exception as ex:
            return Response(
                f'Database error {ex}'
            )
        return Response(self.OutputSerializer(car).data)



