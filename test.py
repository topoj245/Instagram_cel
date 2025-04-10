# import pandas as pd
# import os

# from appium import webdriver
# from appium.webdriver.webdriver import AppiumOptions
# from time import sleep 
# from appium.webdriver.common.appiumby import AppiumBy


# # Librerias de prueba
# import commands_adb as adb
# import random

# from commands_adb import get_connect_devices

# import socket
# import subprocess
# from time import time

from dash import Dash, html, dcc, Input, Output

import pyodbc

# a = [4, 1] 
# b = [{'type': 'boton', 'filename': '9981656564.csv'}, {'type': 'boton', 'filename': '9988744863.csv'}, {'type': 'boton', 'filename': 'hola.csv'}]

# for ad, bd in zip(a, b):
#     print(ad, bd)

print(pyodbc.drivers())

# App = Dash(__name__, routes_pathname_prefix='/Ejemplo/', suppress_callback_exceptions=True)

# App.layout = html.Div([
#     html.H1("Sistema de Gestión de Archivos"),
#     dcc.Upload(
#         id='Upload-data',
#         children=html.Button('Subir Archivo'),
#         multiple=False
#     ),
#     html.Div(id='output-upload'),
#     html.Ul(id='file-list'),
#     html.Button('Cerrar sessión', id = 'logout-button')
# ])

# @App.callback(
#     Output("output", "children"),
#     Input("input1", "value"),
# )
# def haz_algo(valor):
#     if not valor:
#         return "Escribe Algo"
#     return f'Haz escrito esto: {valor}'

# if __name__ == '__main__':    
#     App.run_server(debug=True)

    #Verificar si se debe crear un url para cada dispositivo
# appium_url = "http://127.0.0.1:4723"



# for emulator in get_connect_devices():

#     capabilities = dict(
#     platformName =  'Android',
#     automationName = 'UiAutomator2',
#     platformVersion = '9.0',
#     # El lenguaje es solo mientras dure la conexion de appium, si se reinicia el dispositivo se cambia el idioma
#     language='en',  # Para que todos los dispositivos tengan el mismo idioma local
#     locale='US',
#     noReset = True, 
#     # full_reset = False,
#     newComandTimeOut = 10000,
#     deviceName = emulator,
#     udid = emulator
#     )

#     appium_options = AppiumOptions()
#     appium_options.load_capabilities(capabilities)

#     driver = webdriver.Remote(appium_url, options=appium_options)

#     try:
#         el = driver.find_element(by = AppiumBy.XPATH, value = '//*[@resource-id="com.instagram.android:id/row_feed_button_like" and @content-desc="Like"]')
#         el.click()
#     except:
#         print(f'No hizo nada el {driver.capabilities['deviceName']}')



# data = pd.DataFrame({})
# df = pd.DataFrame({
#     'Nombre': ['Ana', 'Luis', 'Juan'],
#     'Edad': [23, 34, 45],
#     'Ciudad': ['Madrid','Barcelona', 'Valencia']
# })

# for row, col in enumerate(df):
#     print(f'Asi es como sale: {row}')

#     print(f'Y despues: {col}')


