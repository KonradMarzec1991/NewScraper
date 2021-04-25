"""
URLs module
"""

from django.urls import path
from .views import RunNewsLoading

urlpatterns = [
    path('load/', RunNewsLoading.as_view(), name='load')
]
