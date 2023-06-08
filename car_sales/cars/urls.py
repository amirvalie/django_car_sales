from django.urls import path
from . import apis

urlpatterns = [
    path('create-car/', apis.CreateCarApi.as_view(), name='create-car'),
    path('update-car/<int:car_id>/', apis.UpdateCarApi.as_view(), name='update-car'),
    path('search/cars/<str:query>/', apis.CarSearchAPIView.as_view(), name='search-car'),
]
