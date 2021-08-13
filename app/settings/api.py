from drf_yasg.inspectors.view import SwaggerAutoSchema
from inflection import camelize

from app.settings import env

DISABLE_THROTTLING = env('DISABLE_THROTTLING', cast=bool, default=False)
MAX_PAGE_SIZE = env('MAX_PAGE_SIZE', cast=int, default=1000)

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],

    'DEFAULT_PAGINATION_CLASS': 'app.api.pagination.AppPagination',

    'PAGE_SIZE': env('PAGE_SIZE', cast=int, default=10),

    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',

    'DEFAULT_THROTTLE_RATES': {
        'anon-auth': '10/min',
    },

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],

    'DEFAULT_RENDERER_CLASSES': (
        'app.api.renderers.AppJSONRenderer',
        'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
    ),

    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),

    'JSON_UNDERSCOREIZE': {
        'no_underscore_before_number': True,
    },
}


class CamelCaseOperationIDAutoSchema(SwaggerAutoSchema):
    def get_operation_id(self, operation_keys=None):
        operation_id = super(CamelCaseOperationIDAutoSchema, self).get_operation_id(operation_keys)
        return camelize(operation_id, uppercase_first_letter=False)


SWAGGER_SETTINGS = {
    # 'DEFAULT_AUTO_SCHEMA_CLASS': 'app.settings.CamelCaseOperationIDAutoSchema',
    'TAGS_SORTER': None,
    'OPERATIONS_SORTER': 'alpha',
    'SECURITY_DEFINITIONS': {
        'JWT': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': '---',
        },
    },
}

if env('DEBUG'):
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'].append('rest_framework.authentication.SessionAuthentication')
