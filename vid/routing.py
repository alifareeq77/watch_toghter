# routing.py
from django.urls import re_path

from . import consumer

websocket_urlpatterns2 = [
    re_path(r'ws/control/(?P<room_name>\w+)/', consumer.MyConsumer.as_asgi()),
]
