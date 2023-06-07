from django.urls import path
from . import apis

urlpatterns = [
    path('create-car/', apis.CreateCarApi.as_view(), name='create-car'),
]
