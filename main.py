import requests
import json
from src.functions import *
import src.customClasses as cClass
import PySimpleGUI as sg 
import os.path

input = sg.Input('', tooltip="type here to search for a region's weather", enable_events=True, key='-INPUT-', font=('Arial Bold', 20), expand_x=True, justification='left')

dailyColumn = [
    [sg.Text("Daily data", font=('Ubuntu', 24))],
            [sg.TabGroup([
                [ 
                    sg.Tab('Yesterday', [[sg.Text("null", key='day1data', visible=False)], ], key='day1'),
                    sg.Tab('Today', [[sg.Text("null", key='day2data', visible=False)],], key='day2'),
                    sg.Tab('Tomorrow', [[sg.Text("null", key='day3data', visible=False)],], key='day3'),
                    sg.Tab('Day 4', [[sg.Text("null", key='day4data', visible=False)],], key='day4'),
                    sg.Tab('Day 5', [[sg.Text("null", key='day5data', visible=False)],], key='day5'),
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
    [input],
    [sg.Button("SEARCH")],
    [sg.Column(dailyColumn),
             sg.VSeperator(),
        sg.Column(graphColumn, scrollable=True,  sbar_relief=sg.RELIEF_SOLID, sbar_width=12, sbar_arrow_width=12, expand_y=True, expand_x=True)
    ],
]
window = sg.Window("Simple weather app idk", layout, finalize=True, size=(1280, 720), resizable=True)

while True:
    event, values = window.read()
    window.read()
    if event == "QUIT" or event == sg.WIN_CLOSED or event == "QUIT APPLICATION":
        break
    if event == "SEARCH":
        print("search")
        request:str = values['-INPUT-']
        if len(request) < 1:
            print("Error - input is too short")
        else:
            location = requestLocation(request)
            locationData:cClass.geoResults = location[1]
            if location[0] == 200:
                data = requestWeather(locationData['results'][0])
                weatherData:cClass.weatherData = data[1]
                if data[0] == 200:
                    # weather data ong
                    dailyData = formatDailyInfo(weatherData)
                    days = []
                    for day in dailyData:
                        days.append(day.split('\n')[0])
                        
                    print('Weather get')
                    window['day4'].update(days[3], visible=True)
                    window['day5'].update(days[4], visible=True)

                    window['day1data'].update(dailyData[0], visible=True)
                    window['day2data'].update(dailyData[1], visible=True)
                    window['day3data'].update(dailyData[2], visible=True)
                    window['day4data'].update(dailyData[3], visible=True)
                    window['day5data'].update(dailyData[4], visible=True)
                    
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
                    
                    draw(window['-graphs-'].TKCanvas, plotCustom(time, temp, chance, precip, wind, gust))

                    window.Refresh()
                else:
                    print("Error - failed to retrieve weather data")
            else:
                print("Error - could locate any region with the given input")

window.close()
