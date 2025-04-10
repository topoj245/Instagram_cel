import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
from driver_connection import create_and_run_driver, proccess_queue
from commands_adb import get_connect_devices
from data_base import guardar_registros_en_bd
import threading
from lista import devices


import queue

# Lista de funciones disponibles en la interfaz
list_activity = ["Seguir en Instagram", "Dar Like en Instagram"] #, "Scroll en Instagram", "Seguir instagram - Manual", "Login Facebook"]


# Variables globales
global emulator_listbox, selected_task, selected_emulator

# Función para crear la interfaz principal 
def main():
    global emulator_listbox, selected_task,selected_emulator  

    root = tk.Tk()
    root.title("Gestión de Instagram")
    root.geometry("800x600")

    style = ttk.Style(root)
    style.theme_use('clam')
    style.configure('TNotebook.Tab', font=('Helvetica', 10, 'bold'), padding=[10,5])

    label = ttk.Label(text="Dispositivos conectados", font=("Arial", 12))
    label.pack(pady=10)

    emulator_listbox = tk.Listbox(selectmode=tk.MULTIPLE, width=50, height=15)
    emulator_listbox.pack(pady=10)

    # Muestra los emuladores conectados
    emulators = get_connect_devices()
    #print("Dispositivos conectados:", emulators)  # Mensaje de depuración
    for emulator in emulators:
        emulator_listbox.insert(tk.END, emulator)

    task_frame = tk.Frame(root)
    task_frame.pack(fill=tk.X, pady=5)

    ttk.Label(task_frame, text="Selecciona una tarea:", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=10)
    selected_task = tk.StringVar()
    ttk.Combobox(task_frame, textvariable=selected_task, values=list_activity, state="readonly").pack(side=tk.LEFT)

    ttk.Button(root, text="Ejecutar Tarea", command=execute_task).pack(pady=5)

    root.mainloop()
    

def execute_task():
    task = selected_task.get()
    if not task:
        return messagebox.showwarning("Seleccionar Tarea", "Selecciona una tarea.")
    
    datos_tarea = {"task":task}


    selected_emulators = get_connect_devices() #[emulator_listbox.get(i) for i in emulator_listbox.curselection()]
    # if not selected_emulators:
    #     return messagebox.showwarning("Seleccionar Emuladores", "Selecciona al menos un emulador.")

    if task == "Scroll en Instagram" or task == "Login Facebook":
        datos_tarea["url"] = None  # O simplemente no lo añades a los datos_tarea

    else:
        url = simpledialog.askstring("URL", "Ingresa el URL para la tarea:")
        if not url:
            return messagebox.showwarning("url")
        
        datos_tarea["url"] = url

    create_threading(datos_tarea)


####################################

def create_threading(task):
    global selected_emulator

    port = [4724 ,4725, 4726, 4727, 4728]
    
    devices.clear()
    automation_threads = []

    # device_queue = queue.Queue()

    # for device in get_connect_devices():
    #     device_queue.put(device)

    for emulator in get_connect_devices(): # port:
        try:
            #create_and_run_driver
            thread = threading.Thread(target=create_and_run_driver, args=(emulator,task, 4723,))
            automation_threads.append(thread)
            thread.start()
        except Exception as ex:
            print(f"En el emulator{emulator} error: {ex}")

        # create_and_run_driver(emulator, task)

    # Comprobacion para uso de queue (cola)

        # thread = threading.Thread(target=proccess_queue, args=(device_queue, task, port,))
        # automation_threads.append(thread)
        # thread.start()

    for thread in automation_threads:
        thread.join()

    # for device in devices:
    #     print(device)

    # print(f'Al final devices tiene {len(devices)}')
    guardar_registros_en_bd(devices, 'One' , 'Example', task['task'])

if __name__ == "__main__":
    main()








