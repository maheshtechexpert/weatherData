# weatherData
Assignment Project


Coding execersing is completed using Django Framework.

Problem 1 - Data Modelling - Answer.
---------------------------------
Used MySql as a database to store data.

Design data models using Django ORM models.

Weathe data record model is defined at weatherdata/weatherdata/models.py and the class name is WeatherStationData

Problem 2 -  Ingestion - Answer
-------------------------------

Request Url - upload/weatherdata

Created function upload_weather_data() to insert data into the database

function file location - weatherdata/weatherdata/views.py

upload_weather_data() make sure the followig scenarios:

Using WeatherStationData model inserted data into the database
Dupicate data won't be created if file is uploaded multiple times
prints start time , end time and number of records inserted

Problem 3 - Data Analysis - Answer
--------------------------
Request Url - calculate/summary

Weathe summary model is defined at weatherdata/weatherdata/models.py and the class name is WeatherSummary

Created function calculate_summary() to calculate weater summary

function file location - weatherdata/weatherdata/views.py

calculate_summary() make sure the followig scenarios:

for ever year ,for every weather station calulates Avg maximum temperature in degree celsius
for ever year ,for every weather station calulates Avg minimum temperature in degree celsius
for ever year ,for every weather station calulates Total accumulated precipitation in cm
Inserts calculated data into the database using WeatherSummary model.

Problem 4 - REST API - Answer
----------------------------

Using Django framework creating the follwing ednpoints

api/weather/ - Returns weather data in json
weather/stats/ - Returns calucalated weather summary in json



