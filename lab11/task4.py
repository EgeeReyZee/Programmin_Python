import PySimpleGUI as sg
import random

sg.popup_annoying
layout = [
    [sg.Image('C:/Users/619/Desktop/СибГУТИ/Информатика/lab11/magiccube512.png', background_color=('#0f0f0f'), size=(512, 512))],
    [sg.Text(text='Borders:     ', font=('Impact'), text_color=('#5B008C'), background_color=('#000000')), sg.Input(key='-low-', size=(20, 1), background_color=('#808080'), font=('Impact'), text_color=('#5B008C'), border_width=(0)), sg.Text('    -    ', font=('Impact'), text_color=('#5B008C'), background_color=('#000000')), sg.Input(key='-up-', size=(20,1), font=('Impact'), text_color=('#5B008C'), background_color=('#808080'), border_width=(0)), ],
    [sg.Button('GENERATE',  size=(20, 1), font=('Impact', 40), button_color=('#5B008C' ,'#000000'), border_width=(0))],
    [sg.Text(key='-out-', text_color=('#5B008C'), background_color=('#000000'), font=('Impact', 30), size=(26,1), justification=('centre'))]
]

window = sg.Window('random generator', layout, background_color=('#0f0f0f'))

while True:
    event, value = window.read()
    if event in (None, 'Exit'):
        break
    elif event == 'GENERATE':
        try:
            if int(value['-low-']) < int(value['-up-']):
                out = random.randint(int(value['-low-']), int(value['-up-']))
                window['-out-'].update(out)
            elif int(value['-low-']) >= int(value['-up-']):
                window['-out-'].update('Нижняя граница должна быть меньше верхней')
        except:
            window['-out-'].update('Введите целые числа')
        # if int(value['-low-']) == 619 or int(value['-up-']) == 619 or out == 619:
        #    sg.popup_animated('C:/Users/619/Desktop/СибГУТИ/Информатика/lab11/pashalkas/619.png')
window.close()
