from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import ClosestPoints
from .serializer import ClosestPointsSerializer
from .utils import FindPoints

# Create your views here.
class ClosestControler(viewsets.ModelViewSet):                                  
    queryset = ClosestPoints.objects.all()
    serializer_class = ClosestPointsSerializer
    
    def create(self, request, *args, **kwargs):
        points = list(map(lambda item: tuple(map(int, item.split(','))), request.POST['points'].split(';')))
        x = FindPoints()
        closest_points = x.Points(points)
        
        record = ClosestPoints(closest = closest_points, points =request.POST['points'])
        record.save()
        return Response(status=200)
