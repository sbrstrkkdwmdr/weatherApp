import requests
import json 
import src.customClasses as cClass

def requestLocation(name:str) -> requests.Response:
    baseurl = f'https://geocoding-api.open-meteo.com/v1/search?name={name.replace(" ", "+")}&count=10&language=en&format=json'
    res = requests.get(baseurl)
    saveDataToFile(res.json(), 'locationData.json')
    return res
    
def requestWeather(location:cClass.geolocale) -> requests.Response:
    baseurl = f"https://api.open-meteo.com/v1/forecast?latitude={location['latitude']}&longitude={location['longitude']}"
    baseurl += "&hourly=temperature_2m,precipitation,rain,pressure_msl,windspeed_10m,windgusts_10m,precipitation_probability,showers,snowfall"
    baseurl += "&current_weather=true&forecast_days=3&past_days=2"
    baseurl += "&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_sum,rain_sum,showers_sum,snowfall_sum,precipitation_hours,precipitation_probability_max,precipitation_probability_min,precipitation_probability_mean,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant"
    baseurl += f"&timezone={location['timezone']}"
    res = requests.get(baseurl)
    saveDataToFile(res.json(), 'weatherData.json')
    return res
    
def saveDataToFile(data, path:str):
    with open(path, 'w') as f:
        json.dump(data, f)

def formatWeatherCode(code:int):
    string = ""
    icon = ""
    match code:
        case 0:
            string = 'Clear sky'
            icon = '☀'
        case 1:
            string = 'Mostly clear'
            icon = '🌤'
        case 2:
            string = 'Partly Cloudy'
            icon = '⛅'
        case 3:
            string = 'Overcast'
            icon = '☁'
        case 45:
            string = 'Fog'
            icon = '🌁'
        case 48:
            string = 'Fog' #wtf is deposting rime fog
            icon = '🌁'
        case 51:
            string = 'Light drizzle'
            icon = '🌧'
        case 53:
            string = 'Moderate drizzle'
            icon = '🌧'
        case 55:
            string = 'Heavy drizzle'
            icon = '🌧'
        case 56:
            string = 'Light freezing drizzle'
            icon = '🌧'
        case 57:
            string = 'Heavy freezing drizzle'
            icon = '🌧'
        case 61:
            string = 'Light rain'
            icon = '🌧'
        case 63:
            string = 'Moderate rain'
            icon = '🌧'
        case 65:
            string = 'Heavy rain'
            icon = '🌧'
        case 66:
            string = 'Light freezing rain'
            icon = '🌧'
        case 67:
            string = 'Heavy freezing rain'
            icon = '🌧'
        case 71:
            string = 'Light snow'
            icon = '❄'
        case 73:
            string = 'Moderate snow'
            icon = '❄'
        case 75:
            string = 'Heavy snow'
            icon = '❄'
        case 77:
            string = 'Snow grains'
            icon = '❄'
        case 80:
            string = 'Light showers'
            icon = '🌧'
        case 81:
            string = 'Moderate showers'
            icon = '🌧'
        case 82:
            string = 'Heavy showers'
            icon = '🌧'
        case 85:
            string = 'Light snow showers'
            icon = '❄'
        case 86:
            string = 'Heavy snow showers'
            icon = '❄'
        case 95:
            string = 'Thunderstorms'
            icon = '⛈'
        case 96:
            string = 'Thunderstorms and light hail'
            icon = '⛈'
        case 99:
            string = 'Thunderstorms and heavy hail'
            icon = '⛈'
    
    return {
        string:string,
        icon:icon
    }

def formatDailyInfo(data:cClass.weatherData):
    stringList = []
    counter = 0
    daily = data.daily
    for val in daily.time:
        
        counter+=1
        
