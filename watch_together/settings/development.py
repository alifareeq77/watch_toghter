from .base import *

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

AUTH_USER_MODEL = 'users.User'
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
LOGIN_URL = "/auth/login/"
