import requests
import json
from src.functions import *
import src.customClasses as cClass
import PySimpleGUI as sg 
import os.path

input = sg.Input('', tooltip="type here to search for a region's weather", enable_events=True, key='-INPUT-', font=('Arial Bold', 20), expand_x=True, justification='left')

dailyColumn = [
            [sg.TabGroup([
                [ 
                    sg.Tab('Yesterday', [[sg.Text("null", key='day1data', visible=False)], ], key='day1'),
                    sg.Tab('Today', [[sg.Text("null", key='day2data', visible=False)],], key='day2'),
                    sg.Tab('Tomorrow', [[sg.Text("null", key='day3data', visible=False)],], key='day3'),
                    sg.Tab('Day 4', [[sg.Text("null", key='day4data', visible=False)],], key='day4'),
                    sg.Tab('Day 5', [[sg.Text("null", key='day5data', visible=False)],], key='day5'),
                ]], 
                    key='-tabgroup-', expand_x=True, expand_y=True),
           ]
    ]
graphColumn = [
        [sg.Text("TO DO: fancy line graphs")],
]

layout = [
    [sg.Text("Basic weather application", font=('Arial Bold', 24))], 
    [input],
    [sg.Button("SEARCH")],
    [sg.Column(dailyColumn),
             sg.VSeperator(),
        sg.Column(graphColumn)
    ],
    [sg.Text("Console output", size=18, justification='left')],
    [sg.Multiline(size=(60,15), font='Courier 8', expand_x=True, expand_y=True, write_only=True,
                                    reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True, autoscroll=True, auto_refresh=True)],
                      # [sg.Output(size=(60,15), font='Courier 8', expand_x=True, expand_y=True)]
    [sg.Button("QUIT APPLICATION")]
]
window = sg.Window("Simple weather app idk", layout, size=(720, 720))

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
                    window.Refresh()
                else:
                    print("Error - failed to retrieve weather data")
            else:
                print("Error - could locate any region with the given input")

window.close()
