import socket
import subprocess
import time

def start_appium(port):
    def port_in_use(port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0
        
    while port_in_use(port):
        print(f"Port {port} is in use. Trying another port..")
        port += 1

    appium_command = f"appium -p {port}"

    process = subprocess.Popen(appium_command, creationflags=subprocess.CREATE_NO_WINDOW, shell=True)
    print(f"Appium started on port {port}")

    time.sleep(10)

    return process, port