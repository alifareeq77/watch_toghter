import uuid

import django.conf
from django.db import models

from users.models import User
from watch_together.settings.development import ALLOWED_HOSTS


class Party(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='party_user')
    url = models.CharField(null=False, blank=False, unique=True, max_length=255)
    movie_link = models.URLField(null=False, blank=False)
    uuid = models.UUIDField()

    def __str__(self):
        return self.id

    def generate_url(self):
        unique_url = str(uuid.uuid4())
        self.uuid = unique_url
        return f"http://{ALLOWED_HOSTS[0]}:8000/video/{unique_url}"

    def save(self, *args, **kwargs):
        self.url = self.generate_url()
        super().save(*args, **kwargs)
