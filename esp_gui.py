import PySimpleGUI as sg
import esp
import credentials as cred

#TODO: Add functionality to add loadshedding schedules to a calender, start with generating .ics file
#TODO: Make this an executable

#TODO: Make this selectable on the GUI
#TODO: Find a way to save this locally for use next time

credentials = cred.Credentials()
url = 'https://developer.sepush.co.za/business/2.0/area?id=jhbcitypower2-16-cresta'
payload = {}
headers = {'token':f'{credentials.GetESPApiKey()}'}

esp_caller = esp.ESPCaller(url, payload, headers)
schedules_res = esp_caller.GetNextSchedules()
res_parser = esp.ResponseParser()
parsed_schedules = res_parser.ParseResponse(schedules_res)

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
schedules_text = sg.Text(f'{parsed_schedules}')
layout = [  [schedules_text],
            [sg.Button('Refresh'), sg.Button('Close')] ]

# Create the Window
window = sg.Window('EskomSePush', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks close
        break
    if event == 'Refresh':
        schedules_res = esp_caller.GetNextSchedules()
        parsed_schedules = res_parser.ParseResponse(schedules_res)
        schedules_text.update(value=f'{parsed_schedules}')
window.close()