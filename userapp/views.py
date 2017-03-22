from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from userapp.models import Cricketer
from userapp.serializers import CricketerSerializer


class CricketerApiView(APIView):
    def get(self, request):
        """
        :param request:
        :return: get all the name and id of the users
        """
        c = Cricketer.objects.all().distinct()
        return Response(CricketerSerializer(c, many=True).data, status=status.HTTP_200_OK)

