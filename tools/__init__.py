import PySimpleGUI as sg


def dataTable(array, headings):
    layout = [
        [sg.Table(array, headings, max_col_width=35,
                  auto_size_columns=True,
                  display_row_numbers=True,
                  justification='left',
                  key='-TABLE-',
                  tooltip='Data Table')]
    ]
    window = sg.Window('Data Table', layout)
    while True:
        events, values = window.read()
        if events == '-EXIT-' or events == sg.WIN_CLOSED:
            break
    window.close()

    
def verifyFile(file):
    try:
        open(file, 'rt')
    except FileNotFoundError:
        return False
    else:
        return True


def createFile(file):
    try:
        a = open(file, 'wt+', encoding='cp1252')
        a.close()
    except:
        sg.popup('error')
    else:
        sg.popup('FILE CREATED SUCCESFULLY')


def sendValues(file, values):
    name = values['-NAME-']
    age = values['-AGE-']
    try:
        a = open(file, 'at')
    except:
        sg.popup('ERROR IN FILE OPENING')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            sg.popup('ERROR IN FILE EDITING')
        else:
            sg.popup('INFORMATION SUCCESFULLY SENDED')

def fileRead(file):
    try:
        file = open(file, 'rt')
    except:
        sg.popup('ERROR IN FILE OPENING')
    else:
        values = []
        l = ''
        for i in file.readlines():
            l = i.split(';')
            values.append(l)
        return values
