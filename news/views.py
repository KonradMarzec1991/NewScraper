"""
APIView module
"""

from rest_framework.views import APIView
from rest_framework.response import Response

import news.tasks as tasks
from .serializers import PortalSerialier


class RunNewsLoading(APIView):
    """This view delivers method for loading news data"""

    def post(self, request):
        """POST method for loading news"""
        ser = PortalSerialier(data=request.data)
        ser.is_valid(raise_exception=True)
        portal = ser.data.get('portal')

        method_to_call = getattr(tasks, f'get_{portal}')
        method_to_call()

        return Response('Something works!')
