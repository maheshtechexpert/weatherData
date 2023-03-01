from rest_framework import serializers
from weatherdata.models import WeatherStationData
from weatherdata.models import WeatherSummary

class WeatherStationDataSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = WeatherStationData
		fields = ('station_id','date','max_temp','min_temp','precipitation')

class WeatherSummarySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = WeatherSummary
		fields = ('station_id','year','avg_max_temp','avg_min_temp','total_precipitation')