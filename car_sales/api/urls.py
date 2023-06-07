from django.urls import path, include

urlpatterns = [
    path('users/', include(('car_sales.users.urls', 'users'))),
    path('cars/', include(('car_sales.cars.urls', 'cars'))),
    path('auth/', include(('car_sales.authentication.urls', 'auth'))),
]
