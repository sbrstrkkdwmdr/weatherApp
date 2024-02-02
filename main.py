import requests
import json
from src.functions import *
import src.customClasses as cClass
import PySimpleGUI as sg 
import os.path

input = sg.Input('', enable_events=True, key='-INPUT-', font=('Arial Bold', 20), expand_x=True, justification='left')

dailyColumn = [
        [
            [sg.TabGroup([
                [ 
                    sg.Tab('Today', 'data'),
                    sg.Tab('Tomorrow', 'data'),
                    sg.Tab('Overmorrow', 'data'),
                    sg.Tab('Day 4', 'data'),
                    sg.Tab('Day 5', 'data'),
                ]], 
                    key='-TAB GROUP-', expand_x=True, expand_y=True),
           ]
        ]
    ]

graphColumn = [
        [sg.Text("nbl;gl")],
]

layout = [
    [sg.Text("Hello from PySimpleGUI")], 
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
    if event == "QUIT" or event == sg.WIN_CLOSED:
        break
    if event == "SEARCH":
        window.Title = "uwu"
        request:str = values['-INPUT-']
        if len(request) < 1:
            print("Error - input is too short")
        else:
            location:requests.Response = requestLocation(request)
            locationData:cClass.geoResults = location.json()
            if location.status_code == 200:
                data:requests.Response = requestWeather(locationData['results'][0])
                weatherData:cClass.weatherData = cClass.AttrDict(data.json())
                if data.status_code == 200:
                    # weather data ong
                    dailyData = formatDailyInfo(weatherData)
                    days = []
                    for day in dailyData:
                        days.append(day.split('\n')[0])
                        
                    dailyColumn = [
                        [sg.TabGroup([
                            [ 
                                sg.Tab('Today', dailyInfoToLayout(dailyData[0])),
                                sg.Tab('Tomorrow', dailyInfoToLayout(dailyData[1])),
                                sg.Tab('Day 3', dailyInfoToLayout(dailyData[2])),
                                sg.Tab('Day 4', dailyInfoToLayout(dailyData[3])),
                                sg.Tab('Day 5', dailyInfoToLayout(dailyData[4])),
                                ]], 
                                key='-TAB GROUP-', expand_x=True, expand_y=True),
               ]
                    ]
                    print('Weather get')
                else:
                    print("Error - failed to retrieve weather data")
            else:
                print("Error - could locate any region with the given input")

window.close()
