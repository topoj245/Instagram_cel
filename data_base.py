import pymysql
from datetime import datetime

# Configura la conexión a la base de datos MySQL
DB_CONFIG = {
    "host": "rimgsa.com", 
    "user": "admin_global",
    "password": "adminrimgsa",
    "database": "db_globales"
}

def conectar_bd():
    """
    Crea y devuelve una conexión a la base de datos MySQL utilizando pymysql.
    """
    try:
        conn = pymysql.connect(**DB_CONFIG)
        print("Conexión a la base de datos establecida.")
        return conn
    except pymysql.MySQLError as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

def guardar_registros_en_bd(data, cliente, worker_id, task):
    """
    Guarda los registros en las tablas 'trackers_clients' y 'facebook_records'.

    Args:
        data (list): Lista de listas, donde cada sublista representa un registro (dispositivo, fecha, url, estado).
        cliente (str): Nombre del cliente asociado al registro.
        worker_id (str): Identificador del worker asociado al registro.
    """
    print("Iniciando guardado de registros en la base de datos...")
    print("Datos:", data)
    print("Cliente:", cliente)
    print("Worker ID:", worker_id)
    print("Worker ID:", task)


    if not data:
        print("No hay datos para guardar.")
        return

    conn = conectar_bd()
    if conn:
        try:
            cursor = conn.cursor()

            # Verificar si el cliente ya existe
            print(f"Verificando cliente '{cliente}'...")
            cursor.execute("SELECT id_tracker_client FROM trackers_clients WHERE id_tracker_client = %s", (cliente,))
            cliente_id = cursor.fetchone()
            if not cliente_id:
                print(f"Cliente '{cliente}' no existe. Insertando...")
                cursor.execute("INSERT INTO trackers_clients (name_client) VALUES (%s)", (cliente,))
                conn.commit()
                cliente_id = cursor.lastrowid
                print(f"Cliente '{cliente}' insertado con ID {cliente_id}.")
            else:
                cliente_id = cliente_id[0]
                print(f"Cliente '{cliente}' ya existe con ID {cliente_id}.")

            # Preparar e insertar registros
            print("Preparando registros para insertar...")
            query = """
                INSERT INTO trackers_instagram_records (instagram_device, instagram_date, instagram_url, instagram_task, instagram_condition, instagram_client, instagram_worker_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            registros = [
                (
                    registro[0],  # facebook_device
                    registro[1],  # facebook_date
                    registro[2],  # facebook_url
                    task,  # facebook_task
                    registro[3],  # facebook_condition
                    cliente_id,   # facebook_client
                    worker_id     # facebook_worker_id
                )
                for registro in data
            ]
            print("Ejecutando consulta con registros:", registros)

            cursor.executemany(query, registros)
            conn.commit()

            print(f"Se han guardado {cursor.rowcount} registros para el cliente '{cliente}' y el worker '{worker_id}'.")
        except pymysql.MySQLError as e:
            print(f"Error al guardar los registros: {e}")
            # Registrar el error en un archivo log
            with open("errores.log", "a") as log:
                log.write(f"[{datetime.now()}] Error al guardar registros: {e}\n")
        except Exception as ex:
            print(f"Error inesperado: {ex}")
        finally:
            cursor.close()
            conn.close()
            print("Conexión a la base de datos cerrada.")
    else:
        print("No se pudo conectar a la base de datos. Verifica la configuración.")