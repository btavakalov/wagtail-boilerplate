from drf_spectacular.views import SpectacularJSONAPIView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import include
from django.urls import path

urlpatterns = [
    path('', include('app.urls.wagtail')),

    path('users/', include('users.urls')),

    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    path('schema.json', SpectacularJSONAPIView.as_view(), name='schema-json'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema-json'), name='schema-swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema-json'), name='schema-redoc'),
]
