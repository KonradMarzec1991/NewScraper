from __future__ import (
    absolute_import,
    unicode_literals
)
from celery import shared_task

from .scraper import (
    wp,
    onet,
    interia,
    polsatnews
)


def get_news(page):
    page.get_board()
    return f'{page.title()} news loaded successfully'


@shared_task
def get_wp():
    get_news(wp)


@shared_task
def get_interia():
    get_news(interia)


@shared_task
def get_onet():
    get_news(onet)


@shared_task
def get_polsatnews():
    get_news(polsatnews)
