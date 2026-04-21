#El objetivo del proyecto es que pasen una carpeta de archivos y que el programa los organice alfabéticamente

import os
import shutil

def organizar_archivos(ruta_carpeta):
    #Cambiamos al directorio que el usuario nos ha dado
    if not os.path.exists(ruta_carpeta):
        print("La ruta no existe.")
        return

    # Listamos todos los archivos en esa carpeta
    # os.listdir nos da una lista con los nombres
    archivos = [f for f in os.listdir(ruta_carpeta) if os.path.isfile(os.path.join(ruta_carpeta, f))]
    
    # Ordenamos la lista alfabéticamente
    archivos.sort()

    for nombre_archivo in archivos:
        # Obtenemos la primera letra en mayúscula
        primera_letra = nombre_archivo[0].upper()
        
        # Si no es una letra (por ejemplo un número o símbolo), lo mandamos a 'Otros'
        if not primera_letra.isalpha():
            primera_letra = "Otros"

        # Creamos la ruta de la subcarpeta (ej: Carpeta/A)
        ruta_subcarpeta = os.path.join(ruta_carpeta, primera_letra)

        # Si la subcarpeta no existe, la creamos
        if not os.path.exists(ruta_subcarpeta):
            os.makedirs(ruta_subcarpeta)

        # Movemos el archivo a su nueva ubicación
        ruta_original = os.path.join(ruta_carpeta, nombre_archivo)
        ruta_destino = os.path.join(ruta_subcarpeta, nombre_archivo)
        
        shutil.move(ruta_original, ruta_destino)
        print(f"Movido: {nombre_archivo} -> Carpeta {primera_letra}")

# --- Inicio del programa ---
ruta = input("Introduce la ruta completa de la carpeta a organizar: ")
organizar_archivos(ruta)
print("¡Organización completada!")