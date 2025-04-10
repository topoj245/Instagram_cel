import subprocess
from appium.webdriver.common.appiumby import AppiumBy
import commands_adb as adb
from time import sleep, time
from datetime import datetime
import random



# Función para desbloquear la pantalla
def unlock_screen(driver):
    if driver.is_locked():
        driver.unlock()


# Funcion para detectar un texto
def is_text(driver, xpath):
    try:
        driver.find_element(by=AppiumBy.XPATH, value=xpath)
        return True #driver.capabilities['deviceName']
    except:
        return False


# Función para abrir facebook mediante Appium
def open_facebook(driver):

    try:
        driver.activate_app("com.facebook.katana")
        print(f'Aplicacion abierta en {driver.capabilities["deviceName"]}')

        # Tiempo de espera para abrir la app 
        sleep(25)

        # Aceptar Terminos y condiciones: Al abrir la app por primera vez.
        if is_text(driver, '//android.view.View[@content-desc="Terms and Privacy Policy" and @text="Terms and Privacy Policy"]'):
            driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Continue"]').click()
        # print("Terminos y Condiciones fue aceptado")
    except:
        print(f'Error: Open App Facebook in {driver.capabilities["deviceName"]}')


# Función para abrir instagram mediante Appium
def open_instagram(driver):
   
    try:
        driver.activate_app("com.instagram.android")
        print(f"Aplicacion abierta en {driver.capabilities['deviceName']}")

        
        # Tiempo de espera para abrir la app 
        sleep(15)

        # Aceptar Terminos y condiciones: Al abrir la app por primera vez.
        if is_text(driver, '//android.view.View[@content-desc="Terms and Privacy Policy" and @text="Terms and Privacy Policy"]'):
            driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Continue"]').click()
        # print("Terminos y Condiciones fue aceptado")
    except:
        print(f'Error: Open App Instagram in {driver.capabilities["deviceName"]}')


def login_instagram(driver):

    # Cuardo de "Tienes una cuenta"
    # mensaje = None

    try:
        # mensaje = driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Do you have an account?"]')
        # if mensaje:
        #     print("Se detectó el mensaje 'Do you have an account?'. Cerrando ventana...")
        if is_text(driver, '//android.view.View[@content-desc="Do you have an account?"]'):
            driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Close"]').click()
            # print("Ventana cerrada correctamente.")
    except:
        print("No se detectó la ventana emergente. Continuando con el programa.")

#-------------------------------------------------
#darle clic a continuar como
    try:
        driver.find_element(AppiumBy.XPATH, '//android.widget.Button[contains(@content-desc, "Continue as")]').click()
        sleep(5)
        driver.find_element(AppiumBy.XPATH, '//android.widget.Button[contains(@content-desc, "Yes, continue")]/android.view.ViewGroup').click()
        sleep(5)
        driver.find_element(AppiumBy.XPATH, '//android.widget.Button[contains(@content-desc, "Sync this info")]/android.view.ViewGroup').click()
        sleep(5)
    
        try:

            usernames = driver.find_elements(AppiumBy.XPATH, '//android.widget.EditText[@text!=""]')

            # Crear una lista para guardar los textos de los EditText
            usernames_list = []

            # Iterar sobre los elementos encontrados y extraer el texto de cada uno
            for username in usernames:
                usernames_list.append(username.text)

            # Abrir el archivo en modo de adición ("a") para no sobrescribirlo
            with open("usernames.txt", "a") as file:
                for username in usernames_list:
                    file.write(username + "\n")
        except:
            print("no se encontro user name")

        driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Next"]/android.view.ViewGroup').click()
        sleep(5)
        driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="I agree"]/android.view.ViewGroup').click()
        sleep(5)
    except:
        print("no se detecto continuar como")
    
    sleep(5)

    try:
        driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button2" and @text="OK"]').click()
    except:
        print("no se encontro el mensaje de error")

    try:
        driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.packageinstaller:id/permission_deny_button"]').click()
    except Exception as e:
        print(f"No se pudo hacer clic en el botón de denegar permiso: {e}")

    sleep(5)

    try:
        driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Home"]').click()
        print("Se hizo clic en el elemento.")
    except Exception as e:
        print(f"No se pudo hacer clic en el elemento: {e}")

    sleep(5)


##-------------------------------------------------------------------------------------------------------------------------------------------------
# Función para dar like a publicaciones
def like_instagram(driver, link = None):
    
    # Variables para la base de datos
    data = [None] * 4
    # start = None
    # end = None
    data[0] = driver.capabilities['deviceName']
    data[1] = datetime.now()
    data[2] = link
    
    # Comienza a medir el tiempo de ejecución
    # start = time()

    # Abrir Instagram mediante link
    if not adb.instagram_link(driver.capabilities['deviceName'], link):
        data[3] = "URl no acceptado"
        return data
    
    sleep(5)

    # Aceptar abrir el link con Instagram - La acción se realizará una vez en cada dispositivo (Por confirmar)
    # if is_text(driver, '//android.widget.TextView[@resource-id="android:id/sem_title_default" and @text="Open with"]'):
    #     driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Instagram"]').click()
    #     driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Instagram"]').click()

    #     sleep(10)
    #     if is_text(driver, '//android.widget.TextView[@text="Instagram"]'):
    #         driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Instagram"]').click()

    #         driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="android:id/button_always"]').click()
    
    #     else: 
    #         print(f'Fallo en el dispositivo {driver.capabilities['deviceName']} acción detenida')
    #         data.append("Aplicación no encotrada")
    #         return data
        
        
    sleep(2)

    public_reel = "https://www.instagram.com/reel/"

    if public_reel in link:
        try:
            # Busca el boton de Like en el rell y le da click
            el = driver.find_element(by = AppiumBy.XPATH, value = '//*[@resource-id="com.instagram.android:id/like_button" and @content-desc="Like"  and @selected="false"]')
            el.click()

        except:
            # Si falla se notificara y se terminara la acción
            print(f"El dispositivo {driver.capabilities['deviceName']} no realizo la acción")
            driver.terminate_app("com.instagram.android")
            data[3] = "No se encontró el botón"
            return data
        
    else:
        try:
            # Busca el boton de Like en la publicación y le da click
            # driver.find_element(by = AppiumBy.XPATH, value = '//android.view.ViewGroup[@resource-id="com.instagram.android:id/row_feed_button_like" and @content-desc="Like"]').click()
            el = driver.find_element(by = AppiumBy.XPATH, value = '//*[@resource-id="com.instagram.android:id/row_feed_button_like" and @content-desc="Like"]')
            el.click()

            # driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value = 'new UiSelector().resourceId("com.instagram.android:id/row_feed_button_like")').click() # .description("Like") "Me gusta"
        except:
            # Si falla se notificara y se terminara la acción
            print(f"El dispositivo {driver.capabilities['deviceName']} no realizo la acción")
            driver.terminate_app("com.instagram.android")
            data[3] = "No se encontró el botón"
            return data
    
    sleep(5)

    # Termina de medir el tiempo de ejecución
    # end = time()

    # Confirmación de la acción - Verifica si se cambio el Xpath de la publicación 
    if is_text(driver, '//*[@resource-id="com.instagram.android:id/row_feed_button_like" and @content-desc = "Liked"]') or is_text(driver, '//*[@resource-id="com.instagram.android:id/like_button" and @content-desc="Like" and @selected="true"]'): # if is_text(driver, '//android.view.ViewGroup[@resource-id="com.instagram.android:id/row_feed_button_like" and @content-desc = "Liked"]'):
        print(f"El dispositivo {driver.capabilities['deviceName']} realizo la acción") #  en {end - start:.2f}
        data[3] = "Like dado"
    else:
        print(f"El dispositivo {driver.capabilities['deviceName']} no realizo la acción")
        data[3] = "Like no dado"

    # Presionar el boton para volver a la pagina de inicio
    driver.press_keycode(4)

    return data


# Función para Seguir perfiles - Opción mediante Link
def follow_instagram(driver, link = None):

    data = [None] * 4

    # Variables para determinar el tiempo
    # start = None
    # end = None
    data[0] = driver.capabilities['deviceName']
    data[1] = datetime.now()
    data[2] = link

    # Comenzar a medir el tiempo de ejecución
    # start = time()

    # Abrir Instagram mediante link
    if not adb.instagram_link(driver.capabilities['deviceName'], link):
        data[3] = "URl no acceptado"
        return data
    
    sleep(5)

    # # Aceptar abrir el link con Instagram - La acción se realizará una vez en cada dispositivo (Por confirmar)
    # if is_text(driver, '//android.widget.TextView[@resource-id="android:id/sem_title_default" and @text="Open with"]'):
    #     driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Instagram"]').click()
    #     sleep(2)
    #     driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="android:id/button_always"]').click()
    # sleep(5)

    try:
        # Busca el boton de Seguir en el perfil y le da click
        el = driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.instagram.android:id/profile_header_follow_button" and @text="Follow"]')
        el.click()   
    except:
        # Si fallá se notificará y se terminará la acción
        print(f'El dispositivo {driver.capabilities["deviceName"]} no realizo la acción')
        driver.terminate_app("com.instagram.android")
        data[3] = "No se encontró el botón"
        return data
    
    # Termina de medir el tiempo de ejecución
    # end = time()

    # Confirmación de la acción - Verifica si se cambio el Xpath de la publicación 
    if is_text(driver, '//*[@resource-id="com.instagram.android:id/profile_header_follow_button" and @text="Following"]'):
        print(f'El dispositivo {driver.capabilities["deviceName"]} realizo la acción')
        data[3] = "Siguiendo cuenta"
    else:
        print(f'El dispositivo {driver.capabilities["deviceName"]} no realizo la acción')
        data[3] = "No se pudo seguir cuenta"

    # Presionar el boton para volver a la pagina de inicio
    driver.press_keycode(4)

    return data

# Función para Seguir perfiles - Opción manual
def dar_seguir(driver, user):

    # Variables para determinar el tiempo
    start = None
    end = None

    # Comenzar a medir el tiempo de ejecución
    start = time()
    
    # Abrir Instagram
    open_instagram(driver)

    try:
        driver.find_element(by = AppiumBy.XPATH, value = '//android.widget.FrameLayout[@content-desc="Search and explore"]').click()
        sleep(2)
        
        driver.find_element(by = AppiumBy.XPATH, value = '//android.widget.FrameLayout[@resource-id="com.instagram.android:id/action_bar_search_hints_text_layout"]').click()
        driver.find_element(by = AppiumBy.XPATH, value = '//android.widget.EditText[@resource-id="com.instagram.android:id/action_bar_search_edit_text"]').send_keys(user)
        sleep(2)
    except:
        print("No se pudo realizar la busqueda")

    try: 
        driver.find_element(by = AppiumBy.XPATH, value = f'//android.widget.TextView[@resource-id="com.instagram.android:id/row_search_user_username" and @text="{user}"]').click()
        sleep(2)
    except:
        print("No se encontro el nombre de usuario")

    try: 
        driver.find_element(by = AppiumBy.XPATH, value = '//android.widget.Button[@text="Follow"]').click()
        end = time()
        sleep(3)
    except:
        print(f'El dispositivo {driver.capabilities["deviceName"]} no realizo la acción')
        driver.terminate_app("com.instagram.android")
        return
    
    # Termina de medir el tiempo de ejecución
    end = time()
    
    # Confirmación de la acción - Verifica si se cambio el Xpath de la publicación 
    if is_text(driver, '//android.widget.Button[@text="Following" and @resource-id="com.instagram.android:id/profile_header_follow_button"]'):
        print(f'El dispositivo {driver.capabilities["deviceName"]} realizo la acción en {end - start:.2f}')
    else:
        print(f'El dispositivo {driver.capabilities["deviceName"]} no realizo la acción')


    # Reiniciar la opcion de busqueda
    driver.find_element(by = AppiumBy.XPATH, value = '//android.widget.FrameLayout[@content-desc="Search and explore"]').click()

    # Volver a Home 
    driver.find_element(by = AppiumBy.XPATH, value = '//android.widget.FrameLayout[@content-desc="Home"]').click()



# Función de scroll para ver reels
def scroll_instagram_scroll(driver, direction="down", duration=500):
    """Realiza el scroll (swipe) en Instagram en el dispositivo Android y da clic en un reel."""
    try:
        # Dar clic en el botón de Reels
        reels_button = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="Reels"]')
        reels_button.click()
        print("Entrando a la sección de Reels.")
        sleep(5)  # Espera para que la sección de Reels cargue completamente

        # Realizar scroll de forma continua
        while True:
            # Seleccionar un reel aleatoriamente
            reels = driver.find_elements(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="com.instagram.android:id/video_container"]')
            if reels:
                reel_to_click = random.choice(reels)  # Seleccionar un reel al azar
                reel_to_click.click()
                print("Reel seleccionado y abierto.")
                
                # Esperar un tiempo aleatorio entre 10 y 20 segundos antes del próximo scroll
                wait_time = random.randint(10, 20)
                print(f"Esperando {wait_time} segundos mientras se visualiza el reel.")
                sleep(wait_time)
                
                # Volver a la lista de Reels (simula un swipe hacia abajo para cerrar el reel)
                driver.back()
                sleep(3)

            # Coordenadas iniciales y finales para el swipe (scroll)
            if direction == "down":
                start_x, start_y, end_x, end_y = 500, 1500, 500, 500
            elif direction == "up":
                start_x, start_y, end_x, end_y = 500, 500, 500, 1500
            else:
                raise ValueError("Dirección no válida. Usa 'down' o 'up'.")

            # Comando ADB para realizar el swipe (scroll)
            subprocess.run(
                ['adb', '-s', driver.capabilities['deviceName'], 'shell', 'input', 'swipe',
                 str(start_x), str(start_y), str(end_x), str(end_y), str(duration)],
                check=True
            )
            print(f"Scroll realizado hacia {direction} en Instagram en el dispositivo {driver.capabilities['deviceName']}.")
            sleep(2)

    except subprocess.CalledProcessError as e:
        print(f"Error al realizar scroll en Instagram en {driver.capabilities['deviceName']}: {e}")
    except ValueError as ve:
        print(ve)
    except Exception as ex:
        print(f"Error desconocido al hacer scroll: {ex}")

# ------------------------------------------------------------------------------------------------------------------------------------
