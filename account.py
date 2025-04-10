import pandas as pd
import comand_adb as adb
import os

"""Esta parte solo funciona para la automatización del login en las cuentas de facebook"""

#####################################################################
# Nombre del archivo que quieres verificar
nombre_archivo = r"C:\Users\Admin\Documents\Visual_Studio\Project_Instagram_03\Cuentas_facebook_02.xlsx" #"C:\appium\cunetas insta\Cuentas_facebook_02.xlsx" # Ruta del archivo de cuentas
new_archivo = "Cuentas_facebook_02.xlsx" # Archivo dentro de la carpeta de proyecto

# Crear un nuevo archivo de cuentas
# Verificar si el archivo existe en la carpeta actual
if not os.path.exists(nombre_archivo):
    
    archivo = pd.read_csv(r"C:\Users\Admin\Documents\Visual_Studio\Project_Instagram_03\Archive\Cuentas_Cesar.csv") #"C:\appium\cunetas insta\Archive\Cuentas_Cesar.csv") # Archivo original de cuentas - Siempre cambiar la ruta del documento

    # Columnas extras
    Colnames = ['asignado', 'in_use', 'device', 'no_box']
    new_columns = pd.DataFrame(columns=Colnames)

    list_account = pd.concat([archivo, new_columns], ignore_index=True)


    list_account['asignado'] = 0
    list_account['in_use'] = 0
    list_account['device'] = None
    list_account['no_box'] = None
  
    list_account.to_excel(new_archivo, index=False)

archivo_account = pd.read_excel(new_archivo)

# def all_cuentas(box):
#     for device in adb.get_connect_devices():
#         if not device in archivo_account['device'].values:
#             for row in archivo_account.itertuples(index=True):
#                 if row.asignado == 0 and not row.in_use == 2:
#                     archivo_account.loc[row.Index, 'asignado'] = 1
#                     archivo_account.loc[row.Index, 'device'] = str(device)
#                     archivo_account.loc[row.Index, 'no_box'] = f'"{box}"'
#                     break
#         else: 
#             return
#     archivo_account.to_excel(new_archivo, index=False)

# Función para asignar una cuenta a cada dispositivo conectado
def asignar_cuentas(device, box):
    # for device in adb.get_connect_devices():
    if not device in archivo_account['device'].values:
        for row in archivo_account.itertuples(index=True):
            if row.asignado == 0 and not row.in_use == 2:
                archivo_account.loc[row.Index, 'asignado'] = 1
                archivo_account.loc[row.Index, 'device'] = str(device)
                archivo_account.loc[row.Index, 'no_box'] = str(box)
                break
    else: 
        return
    archivo_account.to_excel(new_archivo, index=False)

# Función para obtener las cuentas asignadas a los dispositivos
def get_account(device):
    index = archivo_account[archivo_account['device'] == device].index

    return index[0], archivo_account.loc[index[0], 'Correo'], archivo_account.loc[index[0], 'Contraseña']

# Funcion para actualizar el estado de las cuentas
def actualizar_cuenta(index, verify):    
    if verify:
        archivo_account.loc[index, 'in_use'] = 2
        archivo_account.loc[index,"device"] = None
        archivo_account.loc[index,"no_box"] = None
        archivo_account.loc[index,"asignado"] = 0
        archivo_account.to_excel(new_archivo, index=False)
        return

    archivo_account.loc[index, 'in_use'] = 1
    archivo_account.to_excel(new_archivo, index=False)



# all_cuentas("1100018")