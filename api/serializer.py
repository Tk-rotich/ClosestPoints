from rest_framework import serializers
from .models import ClosestPoints

class ClosestPointsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClosestPoints
        fields = ['points', 'closest']