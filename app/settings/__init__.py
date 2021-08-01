import os

import environ
from split_settings.tools import include

env = environ.Env(
    DEBUG=(bool, False),
)

# environ.Env.read_env()

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

SECRET_KEY = env('SECRET_KEY', default='django-insecure-am8u)784_e9j5_p2$7&3l43@yy0h!jpn%nl_!qm@fv_-m*w8s-')

DEBUG = env('DEBUG', cast=bool, default=False)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'

BASE_URL = 'http://example.com'

# SITE_ID = 1
#
include(
    'auth.py',
    # 'api.py',
    'templates.py',
    'db.py',
    # 'email.py',
    # 'http.py',
    'i18n.py',
    'installed_apps.py',
    # 'media.py',
    'middleware.py',
    # 'sentry.py',
    'static.py',
    'timezone.py',
    'wagtail.py',
)
