from __future__ import absolute_import, unicode_literals
from celery import shared_task

from .scraper import Scraper


@shared_task
def get_news():
    Scraper().get_news()
    return 'Loaded successfully'
