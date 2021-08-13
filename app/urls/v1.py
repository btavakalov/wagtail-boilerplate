from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from django.conf.urls import url
from django.urls import include
from django.urls import path

schema_view = get_schema_view(
    openapi.Info(
        title='API',
        default_version='v1',
        contact=openapi.Contact(email=''),
    ),
    public=True,
    patterns=[
        url(r'^api/v1/', include(('app.urls.v1', 'app'), namespace='v1')),
    ],
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)

urlpatterns = [
    path('', include('app.urls.wagtail')),

    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    path('users/', include('users.urls')),

    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-swagger'),
]
