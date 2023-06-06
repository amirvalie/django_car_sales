from django.urls import path, include

urlpatterns = [
    path('car/', include(('car_sales.cars.urls', 'car'))),
]
