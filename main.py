import requests
import json
from src.functions import *
import src.customClasses as cClass
import PySimpleGUI as sg 
import os.path
import src.define as constants

print(f'Testmode is {constants.testmode}')

guiinput = sg.Input('', tooltip="type here to search for a region's weather", enable_events=True, key='-INPUT-', font=('Arial Bold', 20), expand_x=True, justification='left')

regions = []
guilist = sg.Combo([], expand_x=True, font=('Arial', 16), key='-list-', enable_events=True)

tempWeatherStr = "Date\nWeather\n?% chance of rain\nTemperature\nSunrise\nSunset\nwinds\nGusts"

dailyColumn = [
    [sg.Text("Daily data", font=('Ubuntu', 24), key='title')],
            [sg.TabGroup([
                [ 
                    sg.Tab('Yesterday', [[sg.Text(tempWeatherStr, key='day1data')], ], key='day1'),
                    sg.Tab('Today', [[sg.Text(tempWeatherStr, key='day2data')],], key='day2'),
                    sg.Tab('Tomorrow', [[sg.Text(tempWeatherStr, key='day3data')],], key='day3'),
                    sg.Tab('Day 4', [[sg.Text(tempWeatherStr, key='day4data')],], key='day4'),
                    sg.Tab('Day 5', [[sg.Text(tempWeatherStr, key='day5data')],], key='day5'),
                ]], 
                    key='-tabgroup-', expand_x=True, expand_y=True),
           ],
            [sg.Text("Console output", font=('Consolas', 16), justification='left')],
            [sg.Multiline(size=(60,15), font='Courier 8', expand_x=True, expand_y=True, write_only=True,
                                    reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True, autoscroll=True, auto_refresh=True)],
            # [sg.Output(size=(60,15), font='Courier 8', expand_x=True, expand_y=True)]
            [sg.Button("QUIT APPLICATION")]
    ]
graphColumn = [
        [sg.Text("Graphs", font=('Ubuntu', 24))],
        [sg.Canvas(size=(700,700), key="-graphs-")],
]

layout = [
    [sg.Text("Basic weather application", font=('Arial Bold', 24))], 
    [sg.Text("Search for a region here", font=('Ubuntu', 16))],
    [guiinput],
    [guilist],
    [sg.Button("SEARCH")],
    [sg.Column(dailyColumn),
             sg.VSeperator(),
        sg.Column(graphColumn, scrollable=True,  sbar_relief=sg.RELIEF_SOLID, sbar_width=12, sbar_arrow_width=12, expand_y=True, expand_x=True)
    ],
]
window = sg.Window("Simple weather app idk", layout, finalize=True, size=(1280, 720), resizable=True)

window.Element('day2').Select()

def returnWeather(locationData, index):
    data = requestWeather(locationData['results'][index])
    weatherData:cClass.weatherData = data[1]
    if data[0] == 200:
        # weather data ong
        dailyData = formatDailyInfo(weatherData)
        days = []
        for day in dailyData:
            days.append(day.split('\n')[0])
            
        print('Weather data success')
        window['day4'].update(days[3], visible=True)
        window['day5'].update(days[4], visible=True)

        window['day1data'].update(dailyData[0], visible=True)
        window['day2data'].update(dailyData[1], visible=True)
        window['day3data'].update(dailyData[2], visible=True)
        window['day4data'].update(dailyData[3], visible=True)
        window['day5data'].update(dailyData[4], visible=True)
        
        locationFR = locationData['results'][index]
        window['title'].update(f'Daily data for {locationFR["name"]}, {locationFR["country"]}')
        
        dataObject = weatherData['hourly']
        time = []
        count = 0
        for hour in dataObject['time']:
            if count % 24 == 0:
                time.append(hour.split('T')[0])
            else:
                time.append(f'{count}')
            count+=1
            
        
        # time = dataObject['time']
        temp = dataObject['temperature_2m']
        chance = dataObject['precipitation_probability']
        precip = dataObject['precipitation']
        wind = dataObject['windspeed_10m']
        gust = dataObject['windgusts_10m']
        # 
        window['-graphs-'].TKCanvas.delete("all")
        draw(window['-graphs-'].TKCanvas, plotCustom(time, temp, chance, precip, wind, gust))
        print('Finished graphs')
        window.Refresh()
    else:
        print(constants.errors['noweather'])
        sg.popup(constants.errors['noweather'])

while True:
    event, values = window.read()
    if event == "QUIT" or event == sg.WIN_CLOSED or event == "QUIT APPLICATION":
        break
    if event == "SEARCH":
        print("search")
        request:str = values['-INPUT-']
        if len(request) < 1:
            print(constants.errors['chiinput'])
            sg.popup(constants.errors['chiinput'])
        else:
            location = requestLocation(request)
            locationData:cClass.geoResults = location[1]
            if location[0] == 200:
                print('Location data success')
                if len(locationData['results']) < 1:
                    print(constants.errors['nolocat'])
                    sg.popup(constants.errors['nolocat'])
                else: 
                    regions = []
                    for region in locationData['results']:
                        regions.append(f'{region["name"]}/{region["country"]} ({region["latitude"]},{region["longitude"]})')    
                    window['-list-'].update(values=regions, value=values['-list-'])
                    returnWeather(locationData, 0)
            else:
                print(constants.errors['nolocat'])
    elif event == "-list-":
        tempLocation = values['-list-']
        index = regions.index(tempLocation)
        returnWeather(locationData, index)
window.close()
