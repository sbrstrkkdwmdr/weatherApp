import requests
import json
from src.functions import *
import src.customClasses as cClass
import PySimpleGUI as sg 
import os.path

input = sg.Input('', enable_events=True, key='-INPUT-', font=('Arial Bold', 20), expand_x=True, justification='left')

dailyColumn = [
            [sg.TabGroup([
                [ 
                    sg.Tab('Today', [[sg.Text("null")],]),
                    sg.Tab('Tomorrow', [[sg.Text("null")],]),
                    sg.Tab('Day 3', [[sg.Text("null")],]),
                    sg.Tab('Day 4', [[sg.Text("null")],]),
                    sg.Tab('Day 5', [[sg.Text("null")],]),
                ]], 
                    key='-tabgroup-', expand_x=True, expand_y=True),
           ]
    ]
graphColumn = [
        [sg.Text("nbl;gl")],
]

layout = [
    [sg.Text("Basic weather application")], 
    [input],
    [sg.Button("SEARCH")],
    [sg.Column(dailyColumn),
             sg.VSeperator(),
        sg.Column(graphColumn)
    ],
    [sg.Button("QUIT")],
    [sg.Multiline(size=(60,15), font='Courier 8', expand_x=True, expand_y=True, write_only=True,
                                    reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True, autoscroll=True, auto_refresh=True)]
                      # [sg.Output(size=(60,15), font='Courier 8', expand_x=True, expand_y=True)]
                      
]
window = sg.Window("Simple weather app idk", layout, size=(720, 720))

while True:
    event, values = window.read()
    window.read()
    if event == "QUIT" or event == sg.WIN_CLOSED:
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
                    window['-tabgroup-'].update([ 
                                sg.Tab('Today', dailyInfoToLayout(dailyData[0])),
                                sg.Tab('Tomorrow', dailyInfoToLayout(dailyData[1])),
                                sg.Tab('Day 3', dailyInfoToLayout(dailyData[2])),
                                sg.Tab('Day 4', dailyInfoToLayout(dailyData[3])),
                                sg.Tab('Day 5', dailyInfoToLayout(dailyData[4])),
                                ])
                    window.Refresh()
                else:
                    print("Error - failed to retrieve weather data")
            else:
                print("Error - could locate any region with the given input")

window.close()
