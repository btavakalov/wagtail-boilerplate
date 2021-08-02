from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path

from search import views as search_views

urlpatterns = [
    path('api/v1/', include('app.urls.v1')),
    path('django-admin/', admin.site.urls),
    path('admin/', include(wagtailadmin_urls)),

    path('documents/', include(wagtaildocs_urls)),
    path('search/', search_views.search, name='search'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    path('', include(wagtail_urls)),
]
