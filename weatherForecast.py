import os
import requests
import json
import time
import pandas as pd
from tabulate import tabulate
from accuWeatherApiFunctions import citySearch
from accuWeatherApiFunctions import forecastFor5Days


APIKEY = os.environ.get("ACCWEATHERAPIKEY")
q = input("Enter City Name: ").lower()
print(f"City Name Entered is {q}")

# FINDING LOCATION KEY FOR REQUIRED CITY 
# ========================================================================================

citySearchURL = "http://dataservice.accuweather.com/locations/v1/cities/search"
payLoad1 = {"apikey": APIKEY, "q": q}

jsonData = citySearch(citySearchURL, payLoad1)

if jsonData != None:
    cityKey = jsonData[0]['Key']
    print(f"Location Key for {q.capitalize()} is {cityKey}")
else:
    cityKey = None
    print(f"Location Key for {q.capitalize()} is {cityKey}")

## GETTING FORECAST
## ========================================================================================

urlFor5DayForecast = f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/{cityKey}"
payLoad2 = {"apikey": APIKEY}

t1 = time.perf_counter()
forecast = forecastFor5Days(urlFor5DayForecast, payLoad2)
t2 = time.perf_counter()

if forecast is not None:
    print("\n")
    print(f"Total time taken to get Forecast of 5 days is {round(t2 - t1, 2)} seconds")
    print("\n")
    print(f"=====================Forecast of 5 Days '{q.capitalize()}'======================================================================================\n")
    print(forecast.to_markdown())
else:
    print("Request had bad syntax or the parameters supplied were invalid or City Not Found")
    


    

