# -*- coding: utf-8 -*-

from conexion import conexion
import PySimpleGUI as sg
from monturas import monturas
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Definir el diseño de la interfaz de usuario
token_acceso,token_tipo=conexion()
layout = [
    [sg.Text('Personaje'), sg.InputText(key='-PERSONAJE-')],
    [sg.Text('Servidor'), sg.InputText(key='-SERVIDOR-')],
    [sg.Button('Enviar'), sg.Button('Cancelar')]
]

# Crear la ventana de la aplicación
window = sg.Window('Mi Aplicación', layout)

# Bucle de eventos para interactuar con la ventana
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        break
    elif event == 'Enviar':
        personaje = str(values['-PERSONAJE-'])
        servidor = str(values['-SERVIDOR-'])
        # Aquí puedes hacer lo que necesites con los valores ingresados
        monturas(personaje,servidor)

# Cerrar la ventana al salir del bucle
window.close()
