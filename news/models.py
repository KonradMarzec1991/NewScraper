from django.db import models


class News(models.Model):
    origin = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    header = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return f'News({self.header})'
