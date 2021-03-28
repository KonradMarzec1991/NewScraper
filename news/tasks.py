from __future__ import absolute_import, unicode_literals
from celery import shared_task

from .scraper import (
    get_wp,
    get_polsat,
    get_interia,
    get_onet
)


@shared_task
def get_news():
    get_onet()
