from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WeatherStationDataSerializer
from .serializers import WeatherSummarySerializer
from weatherdata.models import WeatherStationData
from weatherdata.models import WeatherSummary

# Create your views here.

class WeatherStationDataViewSet(viewsets.ModelViewSet):
	queryset = WeatherStationData.objects.all().order_by('station_id')
	serializer_class = WeatherStationDataSerializer

class WeatherSummaryViewSet(viewsets.ModelViewSet):
	queryset = WeatherSummary.objects.all().order_by('station_id')
	serializer_class = WeatherSummarySerializer