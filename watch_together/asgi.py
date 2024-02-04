"""
ASGI config for watch_together project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.conf import settings
from django.core.asgi import get_asgi_application
if settings.DEBUG is True:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'watch_together.settings.development')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'watch_together.settings.production')
application = get_asgi_application()
