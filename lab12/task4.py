import PySimpleGUI as sg

def to_binary(n):
    return bin(n).replace("0b", "").replace("-", "").zfill(8)

def to_inverse_code(n):
    if n >= 0:
        return to_binary(n)
    n = abs(n)
    binary = to_binary(n)
    inverse = ''.join('1' if bit == '0' else '0' for bit in binary)
    return inverse


def to_complement_code(n):
    if n >= 0:
        return to_binary(n)
    inverse = to_inverse_code(n)
    complement = bin(int(inverse, 2) + 1).replace("0b", "")
    return complement.zfill(8)

layout = [
    [sg.Input(key=('-NUM-'), size=(11), border_width=(10), pad=(0, 0), background_color=('#2B2B2B'), font=('a_LCDNova', 40), text_color=('#870000'))],
    [sg.Text('Прямой код', font=('Bahnschrift', 42), pad=(0, 0), text_color=('#AFAFAF'), background_color=('#1E1E1E'))],
    [sg.Input(key=('-STNUM-'), size=(11), background_color=('#2B2B2B'), pad=(0, 0), border_width=(10), font=('a_LCDNova', 40), text_color=('#870000'))],
    [sg.Text('Обратный код', pad=(0, 0), text_color=('#AFAFAF'), font=('Bahnschrift', 36), background_color=('#1E1E1E'))],
    [sg.Input(key=('-NEGNUM-'), size=(11), background_color=('#2B2B2B'), pad=(0, 0), border_width=(10), font=('a_LCDNova', 40), text_color=('#870000'))],
    [sg.Text('Дополнительный код', pad=(0, 0), font=('Bahnschrift', 24), text_color=('#AFAFAF'), background_color=('#1E1E1E'))],
    [sg.Input(key=('-DOPNUM-'), size=(11), background_color=('#2B2B2B'), pad=(0,0), border_width=(10), font=('a_LCDNova', 40), text_color=('#870000'))],
    [sg.Button('1', size=(3,1), border_width=(6), button_color=('#282828')), sg.Button('2', size=(3,1), border_width=(6), button_color=('#282828')), sg.Button('3', size=(3,1), border_width=(6), button_color=('#282828'))],
    [sg.Button('4', size=(3,1), border_width=(6), button_color=('#282828')), sg.Button('5', size=(3,1), border_width=(6), button_color=('#282828')), sg.Button('6', size=(3,1), border_width=(6), button_color=('#282828'))],
    [sg.Button('7', size=(3,1), border_width=(6), button_color=('#282828')), sg.Button('8', size=(3,1), border_width=(6), button_color=('#282828')), sg.Button('9', size=(3,1), border_width=(6), button_color=('#282828'))],
    [sg.Button('*', size=(3,1), border_width=(6), button_color=('#282828')), sg.Button('0', size=(3,1), border_width=(6), button_color=('#282828')), sg.Button('#', size=(3,1), border_width=(6), button_color=('#282828'))]
]

window = sg.Window('Перевод кодов', layout, background_color=('#1E1E1E'), font=('Crystal', 40))

while True:
    event, value = window.read()
    if event == '#':
        try:
            num = int(value['-NUM-'])
            negative_num = 11111111 ^ int(bin(abs(num))[2::].zfill(8))
            if num >= -128 and num <= 127:
                binar = bin(num).replace("0b", "").replace("-", "").zfill(8)
                binar = binar.replace("0", "2")
                binar = binar.replace("1", "0")
                binar = binar.replace("2", "1")
                inv = to_inverse_code(num)
                comp = to_complement_code(num)
                if num >= 0:
                    window['-STNUM-'].update(bin(num)[2::].zfill(8))
                    window['-NEGNUM-'].update('')
                    window['-DOPNUM-'].update('')
                elif num < 0:
                    window['-STNUM-'].update('')
                    window['-NEGNUM-'].update(inv)
                    window['-DOPNUM-'].update(comp)
            else:    
                window['-STNUM-'].update('ERROR')
                window['-NEGNUM-'].update('ERROR')
                window['-DOPNUM-'].update('ERROR')  
        except:
            print('Error')
            window['-STNUM-'].update('ERROR')
            window['-NEGNUM-'].update('ERROR')
            window['-DOPNUM-'].update('ERROR')
    elif event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        window['-NUM-'].update(value['-NUM-']+event)
    elif event == '*':
        window['-NUM-'].update(value['-NUM-'][:-1:])
    elif event in (None, 'Exit'):
        break

window.close()