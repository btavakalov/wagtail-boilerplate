from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.user.is_staff:
            return request.method in SAFE_METHODS
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return True


class IsSuperuserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or request.user and request.user.is_superuser)
