from datetime import datetime

from django.db import models

__all__ = [
    'DefaultModel',
]


class DefaultModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # type: datetime
    updated_at = models.DateTimeField(auto_now=True)  # type: datetime

    objects = models.Manager()

    def __str__(self):
        """Default name for all models"""
        if hasattr(self, 'name'):
            return str(self.name)

        return super().__str__()

    class Meta:
        abstract = True
