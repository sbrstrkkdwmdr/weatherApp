import requests
import json
from src.functions import *
import src.customClasses as cClass
import PySimpleGUI as sg 
import os.path

input = sg.Input('', enable_events=True, key='-INPUT-', font=('Arial Bold', 20), expand_x=True, justification='left')

layout = [
    [sg.Text("Hello from PySimpleGUI")], 
    [input],
    [sg.Button("SEARCH")],
    [sg.Button("QUIT")]
]
window = sg.Window("Demo", layout, size=(400, 400))

while True:
    event, values = window.read()
    if event == "QUIT" or event == sg.WIN_CLOSED:
        break
    if event == "SEARCH":
        request = values['-INPUT-']
        print(request)
        location:requests.Response = requestLocation(request)
        locationData:cClass.geoResults = location.json()
        if location.status_code == 200:
            data:requests.Response = requestWeather(locationData['results'][0])
            weatherData:cClass.weatherData = data.json()
        else:
            print('err')

window.close()
