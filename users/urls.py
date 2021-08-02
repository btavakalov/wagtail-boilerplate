from rest_framework.routers import SimpleRouter

from django.urls import include
from django.urls import path

from users.api.viewsets import UserViewSet

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
