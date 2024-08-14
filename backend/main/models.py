from django.db import models


class CeleryTask(models.Model):
    """ Модель для хранения тасков Celery """

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
