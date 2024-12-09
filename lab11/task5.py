import PySimpleGUI as sg
import time

points = {
    1: ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u'],
    2: ['d', 'g'],
    3: ['b', 'c', 'm', 'p'],
    4: ['f', 'h', 'v', 'w', 'y'],
    5: ['k'],
    8: ['j', 'x'],
    10: ['q', 'z']
}

click_count = 0

layout = [
    [sg.Button('   A   ', font=('Impact', 25), auto_size_button=('True'), button_color=('#BF0000'), border_width=(0)), sg.Button('   B   ', font=('Impact', 25), auto_size_button=('True'), button_color=('#BF3200'), border_width=(0)), sg.Button('   C   ', font=('Impact', 25), auto_size_button=('True'), button_color=('#BC6E00'), border_width=(0)), sg.Button('   D   ', font=('Impact', 25), auto_size_button=('True'), button_color=('#BF9200'), border_width=(0)), sg.Text(' ', background_color=('#4C3200')), sg.Button('   E   ', font=('Impact', 25), auto_size_button=('True'), button_color=('#BFBF00'), border_width=(0)), sg.Text(' ', background_color=('#4C3200')), sg.Button('   F   ', font=('Impact', 25), auto_size_button=('True'), button_color=('#8CBF00'), border_width=(0)), sg.Button('   G   ', font=('Impact', 25), auto_size_button=('True'), button_color=('#49BF00'), border_width=(0)), sg.Button('   H   ', font=('Impact', 25), auto_size_button=('True'), button_color=('#00BF00'), border_width=(0)), sg.Button('   I   ', font=('Impact', 25), auto_size_button=('True'), button_color=('#00BF56'), border_width=(0))],
    [sg.Column([[sg.Button('   V   ', font=('Impact', 25), size=(6, 3), button_color=('#BF000C'), border_width=(0))], [sg.Button('   W   ', font=('Impact', 25), size=(6, 3), button_color=('#BF002F'), border_width=(0))], [sg.Button('   Q   ', font=('Impact', 25), size=(6, 3), button_color=('#BF0054'), border_width=(0))]], background_color=('#4C3200')), sg.Image('Информатика\lab11\letters.png', background_color=('#4C3200')), sg.Column([[sg.Button('   J   ', font=('Impact', 25), size=(6,3), button_color=('#00BF80'), border_width=(0))], [sg.Button('   K   ', font=('Impact', 25), size=(6,3), button_color=('#00BF9C'), border_width=(0))], [sg.Button('   X   ', font=('Impact', 25), size=(6,3), button_color=('#00BFB8'), border_width=(0))]], background_color=('#4C3200'))],
    [sg.Button('   U   ', font=('Impact', 25), auto_size_button=('True'), button_color=('#BF0072'), border_width=(0)), sg.Button('   T   ', font=('Impact', 25), auto_size_button=('True'), button_color=('#9C00BF'), border_width=(0)), sg.Button('   S   ', font=('Impact', 25), auto_size_button=('True'), button_color=('#7900BF'), border_width=(0)), sg.Button('   R   ', font=('Impact', 25), auto_size_button=('True'), button_color=('#4600BF'), border_width=(0)), sg.Button('   P   ', font=('Impact', 25), auto_size_button=('True'), button_color=('#0000BF'), border_width=(0)), sg.Button('   O   ', font=('Impact', 25), auto_size_button=('True'), button_color=('#0029BF'), border_width=(0)), sg.Button('   N   ', font=('Impact', 25), auto_size_button=('True'), button_color=('#0059BF'), border_width=(0)), sg.Button('   M   ', font=('Impact', 25), auto_size_button=('True'), button_color=('#0089BF'), border_width=(0)), sg.Button('   L   ', font=('Impact', 25), auto_size_button=('True'), button_color=('#00BFBF'), border_width=(0))],
    [sg.Text('Enter your word', justification=('centre'), background_color=('#4C3200'), font=('Impact', 30), size=(36))],
    [sg.Input(key=('-WORD-'), font=('Impact', 20), size=(52))],
    [sg.Button('SCORING', size=(9,3), font=('Impact'), border_width=(10), button_color=('#347F0C')), sg.Text(key=('-SCORE-'), font=('Impact', 40), size=(16), justification=('centre')), sg.Image(key=('-PIC-'), background_color=('#4C3200'))]
]

layout2 = [
    [sg.Image(key=('-PASHALKA-'))]
]

window = sg.Window('Word Pointer', layout, background_color=('#4C3200'))
window2 = sg.Window('PASHALKA', layout2, background_color=('#000000'))

while True:
    event, value = window.read()
    letter_list = value['-WORD-']
    total_points = 0
    if event == 'SCORING':
        if letter_list == "Сергей Демин":
            print(letter_list)
            for i in range(10):
                for angle in [0, 45, 90, 135, 180, 225, 270, 315]:
                    window['-PIC-'].update(f"C:/Users/619/Desktop/СибГУТИ/Информатика/lab11/pashalkas/SD{angle}.png")
                    time.sleep(0.1)
                    window.read(timeout=100)
        for letter in letter_list.lower():
            for key, val in points.items():
                if letter in val:
                    total_points += key
                    break
        window['-SCORE-'].update(total_points)
        if total_points <= 10 and total_points > 5:
            window['-PIC-'].update('Информатика\lab11\Dominating.png')
        elif total_points > 10 and total_points <= 20:
            window['-PIC-'].update('Информатика\lab11\Berserk.png')
        #elif total_points > 20 and total_points <= 30:
        #    window['-PIC-'].update('Информатика\lab11\Unstoppable.png')
        elif total_points > 30 and total_points <= 40:
            window['-PIC-'].update('Информатика\lab11\Legendary.png')
        elif total_points > 40:
            window['-PIC-'].update('Информатика\lab11\Godlike.png')
        else:
            window['-PIC-'].update('')
    elif event == '   K   ':
        click_count += 1
        if click_count == 3:
            sg.popup_animated('Информатика/lab11/pashalkas/cartmanKKK.png')
            click_count = 0
    elif event in (None, 'Exit'):
        break

window.close()
window2.close()
