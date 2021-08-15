from rest_framework.request import Request
from wagtail.api.v2.serializers import BaseSerializer
from wagtail.api.v2.serializers import DetailUrlField
from wagtail.api.v2.serializers import PageSerializer

from django.conf import settings


class DefaultDetailUrlField(DetailUrlField):
    def get_attribute(self, instance):
        base_url = getattr(settings, 'WAGTAILAPI_BASE_URL', None)

        model = type(instance)
        router = self.context['router']
        request = self.context['request']  # type: Request
        render_format = request.GET.get('format', None)
        path = router.get_object_detail_urlpath(model, instance.pk)

        if base_url:
            return '{base_url}{path}{format}'.format(
                base_url=base_url,
                path=path,
                format='?format={format}'.format(format=render_format) if render_format else '',
            )

        return '{scheme}://{host}{path}{format}'.format(
            scheme=request.scheme,
            host=request.get_host(),
            path=path,
            format='?format={format}'.format(format=render_format) if render_format else '',
        )

    def to_representation(self, url):
        return url

    def to_internal_value(self, data):
        pass


class CustomBaseSerializer(BaseSerializer):
    detail_url = DefaultDetailUrlField(read_only=True)


class CustomPageSerializer(CustomBaseSerializer, PageSerializer):
    pass
