from django.urls import path, include

urlpatterns = [
    path('cars/', include(('car_sales.cars.urls', 'cars'))),
]
