import PySimpleGUI as sg

import tools

sg.theme('Tan')
file = 'data.txt'
if not tools.verifyFile(file):
    tools.createFile(file)

headings = ['Name', 'Age']

frame = [
    [sg.Text('Name: ')],
    [sg.Input(key='-NAME-', do_not_clear=False)],
    [sg.Text('Age:  ')],
    [sg.Input(key='-AGE-', do_not_clear=False)],
    
]
layout = [
    [sg.Frame('Register', frame)],
    [sg.Button("Registrations", key='-REGISTRATIONS-'),
     sg.Button("Submit", key='-SUBMIT-'),
     sg.Button("Exit", key='-EXIT-')],
]

main_window = sg.Window("Registrations", layout)
while True:
    events, values = main_window.read()
    if events in ('-EXIT-', sg.WIN_CLOSED):
        break
    elif events == '-SUBMIT-':
        tools.sendValues(file, values)
    elif events == '-REGISTRATIONS-':
        values = tools.fileRead(file)
        tools.dataTable(values, headings)
        
main_window.close()
