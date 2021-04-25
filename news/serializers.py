"""
Serializers module
"""

from rest_framework import serializers


class PortalSerialier(serializers.Serializer):
    """Checks if POST request get portal key"""
    portal = serializers.CharField(max_length=20)
