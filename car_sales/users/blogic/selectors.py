from django.shortcuts import get_object_or_404

from ..models import BaseUser


def get_user(pk: int) -> BaseUser:
    return get_object_or_404(BaseUser, pk=pk)

