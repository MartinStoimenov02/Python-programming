# pip install pysimplegui
import PySimpleGUI as sg


def metric_converter(data, in_metric, out_metric):
    metrics = {
        'm': 1, 'mm': 1000, 'cm': 100, 'mi': 0.000621371192, 'dm' : 10, 'mmm' : 1000000, 'nm':1000000000, 'in': 39.3700787, 'km': 0.001, 'ft': 3.2808399, 'yd': 1.0936133,
        'l':1, 'hl':0.01, 'dkl':0.1, 'dl':10, 'kbcm':1000, 'ml':1000,
        'kg':1, 't':0.001, 'kN':0.01, 'hg':10, 'dag':100, 'g':1000, 'karat':5000, 'cg':100000, 'mg':1000000, 'mkg':1000000000, 'ng':1000000000000,
        'm/s':1, 'km/s':0.001, 'km/h':3.6, 'mm/s':1000, 'mph':2.24, 'knot':1.94
    }
    return data/metrics[in_metric]*metrics[out_metric]


sg.theme('BluePurple')

layout = [
    [sg.Text('Input:'),
     sg.InputText(key='-IN-'),
     sg.Combo(('m', 'mm', 'cm', 'mi', 'dm', 'mmm', 'nm', 'in', 'km', 'ft', 'yd', 'l', 'hl', 'dkl', 'dl', 'kbcm', 'ml', 'kg', 't', 'kN', 'hg', 'dag', 'g', 'karat', 'cg', 'mg', 'mkg', 'ng', 'm/s', 'km/s', 'km/h', 'mm/s', 'mph', 'knot'), 'm', readonly=True, key='-IN-M-')],
    [sg.Text('Output:'),
     sg.Text('0', key='-OUT-'),
     sg.Combo(('m', 'mm', 'cm', 'mi', 'dm', 'mmm', 'nm', 'in', 'km', 'ft', 'yd', 'l', 'hl', 'dkl', 'dl', 'kbcm', 'ml', 'kg', 't', 'kN', 'hg', 'dag', 'g', 'karat', 'cg', 'mg', 'mkg', 'ng', 'm/s', 'km/s', 'km/h', 'mm/s', 'mph', 'knot'),
              'm', readonly=True, key='-OUT-M-'),
     sg.Submit('Convert')]
]
window = sg.Window('Metric Converter', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Convert' and values['-IN-'] != '':
        result = metric_converter(
            float(values['-IN-']), values['-IN-M-'], values['-OUT-M-'])
        window['-OUT-'].update(result)
window.close()
