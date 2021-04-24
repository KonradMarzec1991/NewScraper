# pylint: disable=too-few-public-methods
"""
Module contains Django models
"""

from django.db import models


class News(models.Model):
    """Main class for News"""

    origin = models.CharField(max_length=50)
    section = models.CharField(max_length=50, default='main')
    header = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class"""
        verbose_name_plural = 'News'

    def __str__(self):
        return f'News({self.header})'
