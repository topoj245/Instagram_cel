import subprocess

## Función para identificar los dispositivos conectados
def get_connect_devices():
    try:
        result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode('utf-8').strip().split('\n')
        return [line.split('\t')[0] for line in output[1:] if 'device' in line]
    except  Exception as ex:
        print(f"Type-error: {ex}")
        return []

def terimante_facebook(device):
    try:
        subprocess.run(['adb', '-s', device, 'shell', 'am', 'force-stop', '"com.facebook.katana"'], check=True)
    except:
        print(f"Cerrar facebook en {device}")

def desinstall_app():
    apk = 'com.instagram.android'
    try:
        for device in get_connect_devices():
            subprocess.run(['adb', '-s', device, 'shell', 'pm', 'uninstall', apk], check=True)
            print(f"Apk desinstalado en :{device}")
    except Exception as ex:
        print(f"Error al ejecutar el comando: {ex}")


## Función para abrir la app de facebook
def open_facebook(device):
    try:
        subprocess.run(['adb', '-s', device, 'shell', 'am', 'start', '-n', 'com.facebook.katana/com.facebook.katana.activity.FbMainTabActivity'])
    except:
        print(f'No se encontro la app en: {device}')


## Función para abrir la app de instagram
def open_instagram(device):
    try:
        subprocess.run(['adb', '-s', device, 'shell', 'am', 'start', '-n', 'com.instagram.android/com.instagram.mainactivity.InstagramMainActivity'])
    except:
        print(f'No se encontro la app en: {device}')


## Función comprobar que el link prorpocionado sea de instagram
def instagram_link(device, link):
    app = "https://www.instagram.com/"

    if not app in link:
        print("El link propocionado no es de Instagram")
        return  False

    try:
        # Siempre se va a usar driver en lugar de device
        # Cambiar el driver por driver.capabilities['deviceName']
        subprocess.run(['adb', '-s', device, 'shell', 'am', 'start', '-a', 'android.intent.action.VIEW', '-d', link])
        print(f"Link abierto en el dispositivo {device}")
        return True
    except:
          print(f"No se encontró la app en: {device}")
          return False