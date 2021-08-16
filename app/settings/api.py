from app.settings import env

DISABLE_THROTTLING = env('DISABLE_THROTTLING', cast=bool, default=False)
MAX_PAGE_SIZE = env('MAX_PAGE_SIZE', cast=int, default=1000)

REST_USE_JWT = True

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

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
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        # 'djangorestframework_camel_case.parser.CamelCaseFormParser',
        # 'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
    ),

    'JSON_UNDERSCOREIZE': {
        'no_underscore_before_number': True,
    },
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Wagtail Project API',
    'SCHEMA_PATH_PREFIX': '/api/v[0-9]',
    'SCHEMA_PATH_PREFIX_TRIM': True,
    'VERSION': '1.0.0',
    'SERVE_PUBLIC': True,
    'SERVE_INCLUDE_SCHEMA': False,
}

if env('DEBUG'):
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'].append('rest_framework.authentication.SessionAuthentication')
