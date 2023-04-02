import PySimpleGUI as sg
import esp
import credentials as cred

#TODO: Add functionality to add loadshedding schedules to a calender, start with generating .ics file
#TODO: Make this an executable

#TODO: Make this selectable on the GUI
#TODO: Find a way to save this locally for use next time

esp_caller = esp.ESPCaller('jhbcitypower2-16-cresta')
parsed_schedules= esp_caller.get_next_schedules()

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
        parsed_schedules = esp_caller.get_next_schedules()
        schedules_text.update(value=f'{parsed_schedules}')
window.close()