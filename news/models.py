from django.db import models


class News(models.Model):
    origin = models.CharField(max_length=50)
    header = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'News({self.header})'
