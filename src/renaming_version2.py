import os
import utils



def renombrar_expediente(carpeta_origen:str, carpeta_id:str):
    """
    carpeta_id = string del nombre del expediente
    carpeta_origen = Path al archivo donde la carpeta está localizada
    """
    id = carpeta_id
    for nom_archivo in os.listdir(carpeta_origen):
        if nom_archivo.endswith(".pdf"):
            nombre_base = os.path.splitext(nom_archivo)[0]
            if nombre_base == id:
                nuevo_nombre = f"{id}-{utils.conversion_dict['empty']}.pdf"
            else:
                nombre_base = utils.transform_pd_code(nombre_base)
                print(nombre_base)
                nuevo_nombre = f"{id}-{utils.conversion_dict[nombre_base]}.pdf"

            ruta_archivo_viejo = os.path.join(carpeta_origen, nom_archivo)
            ruta_archivo_nuevo = os.path.join(carpeta_origen, nuevo_nombre)
            os.rename(ruta_archivo_viejo, ruta_archivo_nuevo)
            print(f"Renamed {ruta_archivo_viejo} to {ruta_archivo_nuevo}")

def renombrar_archivos_en_carpeta(carpeta_origen, carpeta_id):
    """
    Renames files in the specified folder based on the provided conversion dictionary.
    
    Args:
        carpeta_origen (str): The path to the folder containing the files to rename.
        carpeta_id (int): The ID of the folder.
        conversion_dict (dict): A dictionary mapping old names to new names.
    """
    # Check if the folder exists
    if not os.path.isdir(carpeta_origen):
        print(f"Folder {carpeta_origen} does not exist. Skipping.")
        return

    # Rename files in the folder
    renombrar_expediente(carpeta_origen, carpeta_id)


def renombrar_archivos_en_rango(carpeta_mes, intervalo_inicial, intervalo_final):
    """
    Renames files in folders within the specified range in the month folder.
    
    Args:
        carpeta_mes (str): The path to the month folder.
        intervalo_inicial (int): The starting folder number.
        intervalo_final (int): The ending folder number.
        conversion_dict (dict): A dictionary mapping old names to new names.
    """
    # Iterate through each folder within the specified interval in the month folder
    for i in range(intervalo_inicial, intervalo_final + 1):
        carpeta_origen = os.path.join(carpeta_mes, str(i))

        # Check if the folder exists
        if os.path.isdir(carpeta_origen):
            renombrar_archivos_en_carpeta(carpeta_origen, str(i))
        else:
            print(f"Folder {carpeta_origen} does not exist. Skipping.")


