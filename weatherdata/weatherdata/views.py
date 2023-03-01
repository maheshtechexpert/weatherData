from django.shortcuts import render
from django.views.generic import TemplateView
from weatherdata.models import WeatherStationData
from weatherdata.models import WeatherSummary
from django.db.models import Avg
from django.db.models import Sum
from django.core.files.storage import FileSystemStorage
import csv
import os
from datetime import datetime



def upload_weather_data(request):
	if request.method == 'POST':
		print("Start Time : " , datetime.now())
		weather_data_file = request.FILES['weather_data_file']
		fs = FileSystemStorage()
		weather_data_file_name = fs.save(weather_data_file.name, weather_data_file)
		with open('media/'+weather_data_file_name, "r", encoding="utf8") as station_data:
			tsv_reader = csv.reader(station_data, delimiter="\t")
			station_id = os.path.splitext(weather_data_file.name)[0]
			count = 0
			for row in tsv_reader:
				(date, max_temp, min_temp,precipitation) = row
				#converting to degree celsuis and checking if values are null
				max_temp = float(max_temp)/10 if float(max_temp) != -9999 else None
				min_temp = float(min_temp)/10 if float(min_temp) != -9999 else None
				precipitation = float(precipitation) if float(precipitation) != -9999 else None
				w=WeatherStationData.objects.update_or_create(station_id=station_id,date=date,defaults={'max_temp':max_temp,'min_temp':min_temp,'precipitation':precipitation})
				count = count+1
		print("Total records inserted or updated : " , count)
		print("End Time : ", datetime.now())
		os.remove('media/'+weather_data_file_name)
	return render(request,'upload_weather_data.html')


def calculate_summary(request):
	if request.method == 'POST':
		station = request.POST.get('station')
		year = request.POST.get('year')
		avg_maximum = WeatherStationData.objects.filter(station_id=station).aggregate(Avg('max_temp'))
		avg_minimum = WeatherStationData.objects.filter(station_id=station).aggregate(Avg('min_temp'))
		sum_precipitation = WeatherStationData.objects.filter(station_id=station).aggregate(Sum('precipitation'))
		w=WeatherSummary.objects.update_or_create(station_id=station,year=year,defaults={'avg_max_temp':avg_maximum['max_temp__avg'],'avg_min_temp':avg_minimum['min_temp__avg'],'total_precipitation':sum_precipitation['precipitation__sum']})
	station_ids = list(WeatherStationData.objects.values('station_id').distinct())
	return render(request,'summary.html',{"station_ids": station_ids,'years':range(1984,2015)})	