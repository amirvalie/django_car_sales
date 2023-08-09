from django.urls import path
from . import apis

urlpatterns = [
    path('create-car/', apis.CreateCarApi.as_view(), name='create-car'),
    path('update-car/<int:car_id>/', apis.UpdateCarApi.as_view(), name='update-car'),
    path('search/cars/<str:query>/', apis.CarSearchAPI.as_view(), name='search-car'),
    path('search/car/simple/<str:query>/', apis.CarSearchSimpleAPI.as_view(), name='search-car-simple'),
	path('list-car', apis.ListCarApi.as_view(), name='list-car')
]
