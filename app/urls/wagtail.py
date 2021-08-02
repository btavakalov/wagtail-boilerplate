from wagtail.api.v2.router import WagtailAPIRouter

from django.urls import path

from app.api.wagtail import DocumentsAPIViewSet
from app.api.wagtail import ImagesAPIViewSet
from app.api.wagtail import PagesAPIViewSet

router = WagtailAPIRouter('wagtail')

router.register_endpoint('pages', PagesAPIViewSet)
router.register_endpoint('images', ImagesAPIViewSet)
router.register_endpoint('documents', DocumentsAPIViewSet)

urlpatterns = [
    path('', router.urls),
]
