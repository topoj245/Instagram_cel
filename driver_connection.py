from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions
from time import sleep, time 

import queue

from lista import devices 
# Librerias de prueba
import commands_app as cm


def create_driver(emulator, port):
    #Verificar si se debe crear un url para cada dispositivo
    appium_url = f"http://127.0.0.1:{port}"

    capabilities = dict(
    platformName =  'Android',
    automationName = 'UiAutomator2',
    platformVersion = '9.0',
    # El lenguaje es solo mientras dure la conexion de appium, si se reinicia el dispositivo se cambia el idioma
    language='en',  # Para que todos los dispositivos tengan el mismo idioma local
    locale='US',
    # noReset = True, 
    # full_reset = False,
    newComandTimeOut = 10000,
    deviceName = emulator,
    udid = emulator
    )

    appium_options = AppiumOptions()
    appium_options.load_capabilities(capabilities)

    try:
        driver = webdriver.Remote(appium_url, options=appium_options)
        return driver

    except Exception as ex:
        print(f"Error en crear el driver: {emulator} - {ex}")
        return None

def create_and_run_driver(emulator, task, port):
    data = None

    driver = create_driver(emulator, port)
    if driver is not None:
        try:
            sleep(8)
            if task["task"] == "Dar Like en Instagram":
                data = cm.like_instagram(driver, task["url"])

            elif task["task"] == "Seguir en Instagram":
                data = cm.follow_instagram(driver, task["url"])

            elif task["task"] == "Seguir instagram - Manual":
                data = cm.dar_seguir(driver, task["url"])
            
            elif task["task"] == "Scroll en Instagram":
                data = cm.scroll_instagram(driver)

            elif task["task"] == "Login Facebook":
                data = cm.login_automatic_facebook(driver)

        finally:
            driver.quit()
            if data is not None:
                devices.append(data)
    else:
        print(f"Error en crear el driver: {emulator}")


def proccess_queue(device_queue, task, port):
    while not device_queue.empty():
        try:
            device_name = device_queue.get_nowait()
            create_and_run_driver(device_name, task, port)
        except:
           
            break
        finally:
            device_queue.task_done()