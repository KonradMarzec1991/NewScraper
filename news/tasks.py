"""
Module contains celery tasks
"""

from __future__ import (
    absolute_import,
    unicode_literals
)
from celery import shared_task

from .scraper import wp, onet, interia, polsatnews


@shared_task
def get_wp():
    """Get wp headers"""
    wp.get_board()


@shared_task
def get_interia():
    """Get interia headers"""
    interia.get_board()


@shared_task
def get_onet():
    """Get onet headers"""
    onet.get_board()


@shared_task
def get_polsatnews():
    """Get polsatnews headers"""
    polsatnews.get_board()
