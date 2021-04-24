from __future__ import (
    absolute_import,
    unicode_literals
)
from celery import shared_task

from .scraper import Wp, Onet, Interia, PolsatNews


@shared_task
def get_wp():
    wp = Wp()
    wp.get_board()


@shared_task
def get_interia():
    interia = Interia()
    interia.get_board()


@shared_task
def get_onet():
    onet = Onet()
    onet.get_board()


@shared_task
def get_polsatnews():
    polsatnews = PolsatNews()
    polsatnews.get_board()
