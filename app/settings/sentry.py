from datetime import datetime
import os

from app.settings import env

SENTRY_DSN = env('SENTRY_DSN', cast=str, default=None)

if SENTRY_DSN:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        release=os.environ.get('RELEASE', datetime.now().strftime('%y.%m.%d.%H.%M')),
        traces_sample_rate=1.0,
        send_default_pii=True,
    )
