from collections.abc import Iterable
from django.db import models
from .services import ENCODER


class FTPServer(models.Model):
    host = models.CharField(max_length=255)
    port = models.IntegerField(default=21, blank=True)
    user = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.host

    def save(self):
        self.password = ENCODER.encrypt(self.password)
        super().save()
