from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.core.models import Site
from wagtail.documents.api.v2.views import DocumentsAPIViewSet
from wagtail.images.api.v2.views import ImagesAPIViewSet

from django.conf import settings
from django.http import Http404
from django.urls import path
from django.utils import translation

router = WagtailAPIRouter('wagtail')


class I18nPagesAPIViewSet(PagesAPIViewSet):
    def find_object(self, queryset, request):
        site = Site.find_for_request(request)
        if 'html_path' in request.GET and site is not None:
            path = request.GET['html_path']

            if path == '/':
                language_code = settings.LANGUAGE_CODE
                path_components = path.split('/')
            else:
                language_code, *path_components = [
                    component for component in path.split('/') if component
                ]

            if language_code not in dict(settings.LANGUAGES).keys():
                return

            try:
                page, _, _ = site.root_page.specific.route(request, path_components)
            except Http404:
                return

            if queryset.filter(id=page.id).exists():
                with translation.override(language_code):
                    return page.localized

        return super().find_object(queryset, request)


router.register_endpoint('pages', PagesAPIViewSet)
router.register_endpoint('images', ImagesAPIViewSet)
router.register_endpoint('documents', DocumentsAPIViewSet)

urlpatterns = [
    path('', router.urls),
]
