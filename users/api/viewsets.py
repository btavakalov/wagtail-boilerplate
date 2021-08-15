from app.api.viewsets import DefaultModelViewSet
from users.api.filtersets import UserFilterSet
from users.api.permissions import UserPermission
from users.api.serializers import UserCreateSerializer
from users.api.serializers import UserSerializer
from users.api.serializers import UserUpdateSerializer
from users.models import User


class UserViewSet(DefaultModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    serializer_action_classes = {
        'create': UserCreateSerializer,
        'update': UserUpdateSerializer,
        'partial_update': UserUpdateSerializer,
    }
    permission_classes = (
        UserPermission,
    )
    filterset_class = UserFilterSet
