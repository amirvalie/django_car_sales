from django.urls import path
from .apis import RegisterApi


urlpatterns = [
    path('register/', RegisterApi.as_view(),name="register"),
]
