from django.db import transaction 
from .models import BaseUser

@transaction.atomic
def register(*, email:str, password:str) -> BaseUser:
    user = create_user(email=email, password=password)
    return user
