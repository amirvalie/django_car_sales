from rest_framework.permissions import BasePermission


class IsInSalesGroup(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        elif request.user.groups.filter(name='sales').exists():
            return True
        return False


class IsInSalesGroup(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        elif request.user.groups.filter(name='support').exists():
            return True
        return False
