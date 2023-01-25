# pip install pysimplegui
import PySimpleGUI as sg


def lengh(data, in_metric, out_metric):
    metrics = {
        'm': 1, 'mm': 1000, 'cm': 100, 'mi': 0.000621371192, 'dm' : 10, 'mkm' : 1000000, 'nm':1000000000, 'in': 39.3700787, 'km': 0.001, 'ft': 3.2808399, 'yd': 1.0936133
    }
    return data/metrics[in_metric]*metrics[out_metric]

def volume(data1, in_metric1, out_metric1):
    metrics1 = {
        'l':1, 'hl':0.01, 'dkl':0.1, 'dl':10, 'kb/cm':1000, 'ml':1000
    }
    return data1/metrics1[in_metric1]*metrics1[out_metric1]

def weight(data2, in_metric2, out_metric2):
    metrics2 = {
        'kg':1, 't':0.001, 'kN':0.01, 'hg':10, 'dag':100, 'g':1000, 'karat':5000, 'cg':100000, 'mg':1000000, 'mkg':1000000000, 'ng':1000000000000
    }
    return data2/metrics2[in_metric2]*metrics2[out_metric2]

def speed(data3, in_metric3, out_metric3):
    metrics3 = {
        'm/s':1, 'km/s':0.001, 'km/h':3.6, 'mm/s':1000, 'mph':2.24, 'knot':1.94
    }
    return data3/metrics3[in_metric3]*metrics3[out_metric3]

sg.theme('BrightColors')

layout = [
    [sg.Submit('Lengh'),
    sg.Submit('Volume'),
    sg.Submit('Weight'),
    sg.Submit('Speed')]
]
window1 = sg.Window('Metric Converter', layout)

while True:
    event_f, values_f = window1.read()
    if event_f == sg.WIN_CLOSED:
        break


    elif event_f == 'Lengh':
        sg.theme('DarkBlue15')
        lengh_m = [
            [sg.Text('Input:'),
             sg.InputText(key='-IN-'),
             sg.Combo(('m', 'mm', 'cm', 'mi', 'dm', 'mkm', 'nm', 'in', 'km', 'ft', 'yd'), 'm', readonly=True, key='-IN-M-')],
            [sg.Text('Output:'),
             sg.Text('0', key='-OUT-'),
             sg.Combo(('m', 'mm', 'cm', 'mi', 'dm', 'mkm', 'nm', 'in', 'km', 'ft', 'yd'),
                      'm', readonly=True, key='-OUT-M-'),
             sg.Submit('Convert')]
        ]
        window = sg.Window('Metric Converter-lengh', lengh_m)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Convert' and values['-IN-'] != '':
                result = lengh(float(values['-IN-']), values['-IN-M-'], values['-OUT-M-'])
                window['-OUT-'].update(result)
        window.close()
    

    elif event_f == 'Volume':
        sg.theme('DarkGreen2')
        Volume_m = [
            [sg.Text('Input:'),
             sg.InputText(key='-IN-'),
             sg.Combo(('l', 'hl', 'dkl', 'dl', 'kb/cm', 'ml'), 'l', readonly=True, key='-IN-M-')],
            [sg.Text('Output:'),
             sg.Text('0', key='-OUT-'),
             sg.Combo(('l', 'hl', 'dkl', 'dl', 'kb/cm', 'ml'),
                      'l', readonly=True, key='-OUT-M-'),
             sg.Submit('Convert')]
        ]
        window = sg.Window('Metric Converter-Volume', Volume_m)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Convert' and values['-IN-'] != '':
                result = volume(
                    float(values['-IN-']), values['-IN-M-'], values['-OUT-M-'])
                window['-OUT-'].update(result)
        window.close()
    

    elif event_f == 'Weight':
        sg.theme('DarkTeal')
        weight_m = [
            [sg.Text('Input:'),
             sg.InputText(key='-IN-'),
             sg.Combo(('kg', 't', 'kN', 'hg', 'dag', 'g', 'karat', 'cg', 'mg', 'mkg', 'ng'), 'kg', readonly=True, key='-IN-M-')],
            [sg.Text('Output:'),
             sg.Text('0', key='-OUT-'),
             sg.Combo(('kg', 't', 'kN', 'hg', 'dag', 'g', 'karat', 'cg', 'mg', 'mkg', 'ng'),
                      'kg', readonly=True, key='-OUT-M-'),
             sg.Submit('Convert')]
        ]
        window = sg.Window('Metric Converter-Weight', weight_m)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Convert' and values['-IN-'] != '':
                result = weight(
                    float(values['-IN-']), values['-IN-M-'], values['-OUT-M-'])
                window['-OUT-'].update(result)
        window.close()


    elif event_f == 'Speed':
        sg.theme('DarkRed1')
        speed_m = [
            [sg.Text('Input:'),
             sg.InputText(key='-IN-'),
             sg.Combo(('m/s', 'km/s', 'km/h', 'mm/s', 'mph', 'knot'), 'm/s', readonly=True, key='-IN-M-')],
            [sg.Text('Output:'),
             sg.Text('0', key='-OUT-'),
             sg.Combo(('m/s', 'km/s', 'km/h', 'mm/s', 'mph', 'knot'),
                      'm/s', readonly=True, key='-OUT-M-'),
             sg.Submit('Convert')]
        ]
        window = sg.Window('Metric Converter-Speed', speed_m)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Convert' and values['-IN-'] != '':
                result = speed(
                    float(values['-IN-']), values['-IN-M-'], values['-OUT-M-'])
                window['-OUT-'].update(result)
        window.close()

window1.close()