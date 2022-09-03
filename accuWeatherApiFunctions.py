import requests
import json
import time
import pandas as pd


forecast_of_5_days = []


def citySearch(citySearchURL, payLoad1):
    response = requests.get(citySearchURL, params = payLoad1)
    if (response.status_code == 200) and (response.text != 'null'):
        #print("Success | Status Code: ", response.status_code)
        #print("\n")
        #print("Headers: ", response.headers)
        #print("Request body:", response.request.body)
        #print("Text: ", response.text[0:100])
        
        jsonData = json.loads(response.text)
        if len(jsonData) > 0:
            return jsonData
        else:
            return None
        
    elif (response.status_code == 200) and (response.text == 'null'):
        print("City Not Found")
        return None
    else:
        print(f"Status Code: {response.status_code}")
        return None
    

def forecastFor5Days(urlFor5DayForecast, payLoad2):
    response = requests.get(urlFor5DayForecast, params = payLoad2)
    if (response.status_code == 200) and (response.text != 'null'):
        #print("Success | Status Code: ", response.status_code)
        print("\n")
        #print("Headers: ", response.headers)
        #print("Request body:", response.request.body)
        #print("Text: ", response.text[0:100])

        forecast = json.loads(response.text) #returns json

        # Now parsing json and converting into dataframe
        for i in range(0, 5, 1):
            day = {"Date": forecast['DailyForecasts'][i]['Date'], 
                    "minTemp": forecast['DailyForecasts'][i]['Temperature']['Minimum']['Value'],
                    "maxTemp": forecast['DailyForecasts'][i]['Temperature']['Maximum']['Value'],
                    "Day": forecast['DailyForecasts'][i]['Day']['IconPhrase'],
                    "Day Precipitation": forecast['DailyForecasts'][i]['Day']['HasPrecipitation'],
                    "Night": forecast['DailyForecasts'][i]['Night']['IconPhrase'],
                    "Night Precipitation": forecast['DailyForecasts'][i]['Night']['HasPrecipitation']
                   }

            forecast_of_5_days.append(day)
            time.sleep(response.elapsed.total_seconds())

            print(f"Got Forecast of the day {i + 1} in {round(response.elapsed.total_seconds(), 2)} seconds")

        df = pd.DataFrame(forecast_of_5_days)

        return df
        
    elif (response.status_code == 200) and (response.text == 'null'):
        print("Not Found")
        return None
    else:
        print(f"Status Code: {response.status_code}")
        return None
    
    

