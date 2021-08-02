from app.api.viewsets import DefaultModelViewSet
from users.api import filtersets
from users.api import permissions
from users.api import serializers
from users.models import User


class UserViewSet(DefaultModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    serializer_action_classes = {
        'create': serializers.UserCreateSerializer,
        'update': serializers.UserUpdateSerializer,
        'partial_update': serializers.UserUpdateSerializer,
    }
    permission_classes = (
        permissions.UserPermission,
    )
    filterset_class = filtersets.UserFilterSet
