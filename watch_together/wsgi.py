"""
WSGI config for watch_together project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.conf import settings
from django.core.wsgi import get_wsgi_application
if settings.DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'watch_together.settings.development')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'watch_together.settings.production')
application = get_wsgi_application()
