"""
ASGI config for watch_together project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.conf import settings
from django.core.asgi import get_asgi_application
from vid import routing


if settings.DEBUG is True:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'watch_together.settings.development')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'watch_together.settings.production')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns2))
        ),
    }
)
