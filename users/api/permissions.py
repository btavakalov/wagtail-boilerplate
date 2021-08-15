from rest_framework.permissions import BasePermission

SAFE_ACTIONS = (
    'retrieve',
)


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or view.action in SAFE_ACTIONS

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj == request.user
