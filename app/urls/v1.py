from drf_spectacular.views import SpectacularJSONAPIView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView

from django.urls import include
from django.urls import path

urlpatterns = [
    path('', include('app.urls.wagtail')),

    path('auth/', include('app.urls.auth')),

    path('users/', include('users.urls')),

    path('schema.json', SpectacularJSONAPIView.as_view(), name='schema-json'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema-json'), name='schema-swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema-json'), name='schema-redoc'),
]
