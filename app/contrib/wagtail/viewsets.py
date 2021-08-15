from djangorestframework_camel_case.render import CamelCaseBrowsableAPIRenderer
from drf_spectacular.utils import extend_schema
from wagtail.api.v2.views import PagesAPIViewSet as BasePagesAPIViewSet
from wagtail.core.models import Site
from wagtail.documents.api.v2.views import DocumentsAPIViewSet as BaseDocumentsAPIViewSet
from wagtail.images.api.v2.views import ImagesAPIViewSet as BaseImagesAPIViewSet

from django.conf import settings
from django.http import Http404
from django.utils import translation

from app.api.renderers import AppJSONRenderer
from app.contrib.wagtail.serializer import CustomPageSerializer


class DefaultWagtailViewSet:
    renderer_classes = [AppJSONRenderer, CamelCaseBrowsableAPIRenderer]


class PagesAPIViewSet(DefaultWagtailViewSet, BasePagesAPIViewSet):
    base_serializer_class = CustomPageSerializer

    @extend_schema(
        operation_id='pages_list',
    )
    def listing_view(self, request):
        return super().listing_view(request)

    @extend_schema(
        operation_id='pages_retrieve',
    )
    def detail_view(self, request, pk):
        return super().detail_view(request, pk)


class DocumentsAPIViewSet(DefaultWagtailViewSet, BaseDocumentsAPIViewSet):
    @extend_schema(
        operation_id='documents_list',
    )
    def listing_view(self, request):
        return super().listing_view(request)

    @extend_schema(
        operation_id='documents_retrieve',
    )
    def detail_view(self, request, pk):
        return super().detail_view(request, pk)


class ImagesAPIViewSet(DefaultWagtailViewSet, BaseImagesAPIViewSet):
    @extend_schema(
        operation_id='images_list',
    )
    def listing_view(self, request):
        return super().listing_view(request)

    @extend_schema(
        operation_id='images_retrieve',
    )
    def detail_view(self, request, pk):
        return super().detail_view(request, pk)


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
