from django.db import models

class WeatherStationData(models.Model):
	station_id = models.CharField(max_length=100)
	date = models.DateField()
	max_temp = models.FloatField(null=True)
	min_temp = models.FloatField(null=True)
	precipitation = models.FloatField(null=True)

	class Meta:
		db_table = "weather_station_data"

class WeatherSummary(models.Model):
	station_id = models.CharField(max_length=100)
	year = models.CharField(max_length=10)
	avg_max_temp = models.FloatField()
	avg_min_temp = models.FloatField()
	total_precipitation = models.FloatField()

	class Meta:
		db_table = "weather_summary"