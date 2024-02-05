# routing.py
from django.urls import path

from . import consumer

websocket_urlpatterns2 = [
    path('ws/control/<uuid>/', consumer.MyConsumer.as_asgi()),
]
