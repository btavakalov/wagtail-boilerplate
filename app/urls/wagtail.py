from wagtail.api.v2.router import WagtailAPIRouter

from django.urls import include
from django.urls import path

from app.api.wagtail import DocumentsAPIViewSet
from app.api.wagtail import ImagesAPIViewSet
from app.api.wagtail import PagesAPIViewSet

api_version = 'v1'
app_name = 'wagtailapi'

router = WagtailAPIRouter(f'{api_version}:{app_name}')
router.register_endpoint('pages', PagesAPIViewSet)
router.register_endpoint('images', ImagesAPIViewSet)
router.register_endpoint('documents', DocumentsAPIViewSet)

urlpatterns = [
    path('', include(router.get_urlpatterns())),
]
