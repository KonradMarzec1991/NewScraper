"""
APIView module
"""

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PortalSerialier
from .tasks import (
    get_wp,
    get_onet,
    get_interia,
    get_polsatnews
)


class RunNewsLoading(APIView):
    """This view delivers method for loading news data"""

    def post(self, request):
        """POST method for loading news"""
        ser = PortalSerialier(data=request.data)
        ser.is_valid(raise_exception=True)

        portal = ser.data
        if portal == 'onet':
            get_onet()
        if portal == 'wp':
            get_wp()
        if portal == 'interia':
            get_interia()
        if portal == 'polsatnews':
            get_polsatnews()

        return Response('Something works!')
