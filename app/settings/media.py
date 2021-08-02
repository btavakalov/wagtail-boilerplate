import os

from app.settings import env
from app.settings import PROJECT_DIR

MEDIA_ROOT = env('MEDIA_ROOT', cast=str, default=os.path.join(PROJECT_DIR, 'media'))

MEDIA_URL = '/m/'
