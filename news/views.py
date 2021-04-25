"""
APIView module
"""


from rest_framework.views import APIView
from rest_framework.response import Response


class RunNewsLoading(APIView):
    """This view delivers method for loading news data"""

    def post(self, request):
        """POST method for loading news"""
        portal = request.POST.get('portal')

        print(portal)
        return Response('It works!')
