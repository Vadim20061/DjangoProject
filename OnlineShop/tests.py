from django.db import models
from django.utils import timezone
from django.conf import settings


class Product(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=255)
    created_date = models.DateField(default=timezone.now)
    deadline = models.DateField()
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title