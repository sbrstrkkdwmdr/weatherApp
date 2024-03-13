import requests
import json 
import src.customClasses as cClass
import PySimpleGUI as sg 
import math
import src.define as constants
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def requestLocation(name:str):
    baseurl = f'https://geocoding-api.open-meteo.com/v1/search?name={name.replace(" ", "+")}&count=10&language=en&format=json'
    res:requests.Response = None
    statcode = 404
    if constants.testmode == True:
        print('Getting location data from local file')
        tempfile = open('locationData.json', 'r')
        res = json.load(tempfile)
        tempfile.close()
        statcode = 200
    else:
        print(f'Getting data from {baseurl}')
        restemp = requests.get(baseurl)
        res = restemp.json()
        saveDataToFile(restemp.json(), 'locationData.json')
        statcode = restemp.status_code
    return statcode, res
    
def requestWeather(location:cClass.geolocale):
    baseurl = f"https://api.open-meteo.com/v1/forecast?latitude={location['latitude']}&longitude={location['longitude']}"
    baseurl += "&hourly=temperature_2m,precipitation,rain,pressure_msl,windspeed_10m,windgusts_10m,precipitation_probability,showers,snowfall"
    baseurl += "&current_weather=true&forecast_days=4&past_days=1"
    baseurl += "&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_sum,rain_sum,showers_sum,snowfall_sum,precipitation_hours,precipitation_probability_max,precipitation_probability_min,precipitation_probability_mean,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant"
    baseurl += f"&timezone={location['timezone']}"
    res:requests.Response = None
    statcode = 404
    if constants.testmode == True:
        print('Getting weather data from local file')
        tempfile = open('weatherData.json', 'r')
        res = json.load(tempfile)
        tempfile.close()
        statcode = 200
    else:
        print(f'Getting data from {baseurl}')
        restemp = requests.get(baseurl)
        res = restemp.json()
        saveDataToFile(restemp.json(), 'weatherData.json')
        statcode = restemp.status_code
    return statcode, res
    
def saveDataToFile(data, path:str):
    with open(path, 'w') as f:
        json.dump(data, f)
        f.close()

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
    
    return [
        string,
        icon
    ]

def timeOnly(string:str) -> str:
    split = string.split('T')
    return split[1]

class direction: 
    name: str;
    travels: str;
    emoji: str;
    short: str;
x:direction = {}

def windDirection(angle:float):
    directions:list[direction] = [
        { "name": 'North', "travels": 'South', "emoji": '⬇', "short": 'N', },
        { "name": 'North-Northeast', "travels": 'South-Southwest', "emoji": '↙', "short": 'NNE', },
        { "name": 'Northeast', "travels": 'Southwest', "emoji": '↙', "short": 'NE', },
        { "name": 'East-Northeast', "travels": 'West-Southwest', "emoji": '↙', "short": 'ENE', },
        { "name": 'East', "travels": 'West', "emoji": '⬅', "short": 'E', },
        { "name": 'East-Southeast', "travels": 'West-Northwest', "emoji": '↖', "short": 'ESE', },
        { "name": 'Southeast', "travels": 'Northwest', "emoji": '↖', "short": 'SE', },
        { "name": 'South-Southeast', "travels": 'North-Northwest', "emoji": '↖', "short": 'SSE', },
        { "name": 'South', "travels": 'North', "emoji": '⬆', "short": 'S', },
        { "name": 'South-Southwest', "travels": 'North-Northeast', "emoji": '↗', "short": 'SSW', },
        { "name": 'Southwest', "travels": 'Northeast', "emoji": '↗', "short": 'SW', },
        { "name": 'West-Southwest', "travels": 'East-Northeast', "emoji": '↗', "short": 'WSW', },
        { "name": 'West', "travels": 'East', "emoji": '➡', "short": 'W', },
        { "name": 'West-Northwest', "travels": 'East-Southeast', "emoji": '↘', "short": 'WNW', },
        { "name": 'Northwest', "travels": 'Southeast', "emoji": '↘', "short": 'NW', },
        { "name": 'North-Northwest', "travels": 'South-Southeast', "emoji": '↘', "short": 'NNW', },
        { "name": 'North', "travels": 'South', "emoji": '⬇', "short": 'N', },
        { "name": 'North-Northeast', "travels": 'South-Southwest', "emoji": '↙', "short": 'NNE', },
        { "name": 'Northeast', "travels": 'Southwest', "emoji": '↙', "short": 'NE', },
        { "name": 'East-Northeast', "travels": 'West-Southwest', "emoji": '↙', "short": 'ENE', },
        { "name": 'East', "travels": 'West', "emoji": '⬅', "short": 'E', },
        { "name": 'East-Southeast', "travels": 'West-Northwest', "emoji": '↖', "short": 'ESE', },
        { "name": 'Southeast', "travels": 'Northwest', "emoji": '↖', "short": 'SE', },
        { "name": 'South-Southeast', "travels": 'North-Northwest', "emoji": '↖', "short": 'SSE', },
        { "name": 'South', "travels": 'North', "emoji": '⬆', "short": 'S', },
        { "name": 'South-Southwest', "travels": 'North-Northeast', "emoji": '↗', "short": 'SSW', },
        { "name": 'Southwest', "travels": 'Northeast', "emoji": '↗', "short": 'SW', },
        { "name": 'West-Southwest', "travels": 'East-Northeast', "emoji": '↗', "short": 'WSW', },
        { "name": 'West', "travels": 'East', "emoji": '➡', "short": 'W', },
        { "name": 'West-Northwest', "travels": 'East-Southeast', "emoji": '↘', "short": 'WNW', },
        { "name": 'Northwest', "travels": 'Southeast', "emoji": '↘', "short": 'NW', },
        { "name": 'North-Northwest', "travels": 'South-Southeast', "emoji": '↘', "short": 'NNW', },
    ]
    normalizedAngle = (angle % 360 + 360) % 360
    index = math.floor(normalizedAngle / 22.5)
    return directions[index]

def formatDailyInfo(data:cClass.weatherData):
    stringList = []
    count = 0
    daily = data['daily']
    # weatherType high/low precip% wind->dir+speed(avg)
    for val in daily["time"]:
        weather = formatWeatherCode(daily["weathercode"][count])
        weatherstring = f'{weather[1]}{weather[0]} '
        tempStr = f'High/low temperature: {daily["temperature_2m_max"][count]}°C/{daily["temperature_2m_min"][count]}°C'
        precipNum = ''
        if daily["precipitation_sum"][count] > 0:
            precipNum = f'({daily["precipitation_sum"][count]}mm)'
 
        precipChStr = f'{daily["precipitation_probability_mean"][count]}% chance of rain {precipNum}'
        windDir = windDirection(daily["winddirection_10m_dominant"][count])
        windDirG = windDirection(daily["winddirection_10m_dominant"][count])
        windStr = f'Winds: {daily["windspeed_10m_max"][count]}km/h ({windDir["emoji"]}{windDir["short"]} {daily["winddirection_10m_dominant"][count]}°)'
        windGustStr = f'Gusts: {daily["windgusts_10m_max"][count]}km/h ({windDirG["emoji"]}{windDirG["short"]} {daily["winddirection_10m_dominant"][count]}°)'
        sunrisesetStr = f'Sunrise: {timeOnly(daily["sunrise"][count])}\nSunset: {timeOnly(daily["sunset"][count])}'
        string = f'{val}\n{weatherstring}\n{precipChStr}\n{tempStr}\n{sunrisesetStr}\n{windStr}\n{windGustStr}'
        stringList.append(string)
        count+=1
    return stringList

def dailyInfoToLayout(data:str):
    dataSplit = data.split('\n')
    tempLayout = [
        [sg.Text(dataSplit[0])],
        [sg.Text(dataSplit[1])],
        [sg.Text(dataSplit[2])],
        [sg.Text(dataSplit[3])],
        [sg.Text(dataSplit[4])],
        [sg.Text(dataSplit[5])]
    ]
    return tempLayout
        
def plot(title:str, xName:str, yName:str, xData:list, yData: list, clr,):
    temp = plt
    temp.plot(xData, yData, color=clr,)
    temp.title(title, fontsize=16)
    temp.xlabel(xName, fontsize=12)
    temp.ylabel(yName, fontsize=12)
    temp.grid(True)
    return temp.gcf()
        
def draw(canvas, plot):
    fcta = FigureCanvasTkAgg(plot, canvas)
    fcta.draw()
    fcta.get_tk_widget().pack(side='top', fill='both')
    return fcta

def dailyTicks(x, pos):
    if pos % 24 == 0:
        return x.split('T')[0]
    else:
        return x

def plotCustom(
    time:list[str],
    temp:list[float],
    rainch:list[float],
    precip:list[float],
    wind:list[float],
    windgust:list[float],
):
    print('Generating graphs')
    #rainch and precip together, wind and windgust together
    fig, axs = plt.subplots(3)
    axs[0].plot(time,temp, color='firebrick')
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Temperature (°C)', color='firebrick')
    axs[0].grid(True, linestyle='--', linewidth = 0.5)
    for label in axs[0].xaxis.get_ticklabels():
        if not label.get_position()[0] % 24 == 0:
            label.set_visible(False)
    
    gridlines = axs[0].xaxis.get_gridlines()
    i = 0
    for line in gridlines:
        if i % 12 == 0:
            line.set_color('green')
        if i % 24 == 0:
            line.set_color('red')
        i+=1
            
    axs[1].plot(time, precip, color='deepskyblue')
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Precipitation (mm)', color='deepskyblue')
    axs[1].grid(True, linestyle='--', linewidth = 0.5)
    for label in axs[1].xaxis.get_ticklabels():
        if not label.get_position()[0] % 24 == 0:
            label.set_visible(False)
        
    chanceAx = axs[1].twinx()
    chanceAx.set_ylabel('Chance (%)', color='blue')
    chanceAx.plot(time, rainch, color='blue')
    
    gridlines = axs[1].xaxis.get_gridlines()
    i = 0
    for line in gridlines:
        if i % 12 == 0:
            line.set_color('green')
        if i % 24 == 0:
            line.set_color('red')
        i+=1

        

    axs[2].plot(time, wind, color='forestgreen')
    axs[2].set_xlabel('Time')
    axs[2].set_ylabel('Winds (km/h)', color='forestgreen')
    axs[2].grid(True, linestyle='--', linewidth = 0.5)
    for label in axs[2].xaxis.get_ticklabels():
        if not label.get_position()[0] % 24 == 0:
            label.set_visible(False)
        
    gustAx = axs[2].twinx()
    gustAx.plot(time, windgust, color='orange')
    gustAx.set_ylabel('Gusts (km/h)', color='orange')
    
    gridlines = axs[2].xaxis.get_gridlines()
    i = 0
    for line in gridlines:
        if i % 12 == 0:
            line.set_color('green')
        if i % 24 == 0:
            line.set_color('red')
        i+=1

    fig.tight_layout()
    return fig
    