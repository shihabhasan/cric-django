from __future__ import division
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from userapp.models import Cricketer, RunsByYear
from django.db.models import Sum, FloatField
from django.db.models.functions import Cast
from userapp.serializers import CricketerSerializer


class CricketerApiView(APIView):
    def get(self, request):
        """
        :param request:
        :return: get all the name and id of the users
        """
        c = Cricketer.objects.all().distinct().order_by('id')
        return Response(CricketerSerializer(c, many=True, fields=('id', 'name')).data, status=status.HTTP_200_OK)


class CricketRunApiView(APIView):
    def post(self, request):
        c = Cricketer.objects.filter(id__in=request.data).order_by('id').all().distinct()
        years_available = RunsByYear.objects.all().order_by('year').values_list('year', flat=True).distinct()
        Dict = dict(years=years_available, data=CricketerSerializer(c, many=True).data)
        return Response(Dict, status=status.HTTP_200_OK)


class CricketSummaryApiView(APIView):
    def post(self, request):
        r = RunsByYear.objects.filter(cricketer__id__in=request.data).values('year').annotate(avg=Cast(Sum('run'), FloatField())/Cast(len(request.data), FloatField())).order_by('year').values('year', 'avg')
        years_available = RunsByYear.objects.all().order_by('year').values_list('year', flat=True).distinct()
        Dict = dict(years=years_available, data=r)
        return Response(Dict, status=status.HTTP_200_OK)