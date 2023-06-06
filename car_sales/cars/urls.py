from django.urls import path
from . import apis 


urlpatterns = [
    path('create-car/', apis.CreateCarApi.as_view(), 'car',name='create-car'),

]