import os
import sys
#import treenodepersonal
import re

conversion_dict = {
    'empty': 'ORS-Otros',
    'Paginasdesde': 'CC-Cobertura',
    'Paginasdesde-2': "ActayRecepcion",
    'Paginasdesde-3': "CVC-CodigoValidacion",
    'Paginasdesde-4': "053-Derivacion",
    'Paginasdesde-5': "Inf-Medico",
}

def transform_pd_code(input_string):
    """
    Removes the number after "Paginas desde" from the input string.
    
    Args:
        input_string (str): The input string to transform.
    
    Returns:
        str: The transformed string if a match is found; otherwise, returns the original string.
    """
    if not input_string:
        return input_string
    
    # Pattern:
    # (Paginas[whitespace]desde)    -> captured as group 1
    # \d+                           -> one or more digits (to be removed)
    # ((-\d+)? )                   -> optional dash and number captured as group 2, if present
    pattern = r'(Paginas\s+desde)\d+((-\d+)?)'
    match = re.match(pattern, input_string)
    if match:
        # Reconstruct string using group 1 (the fixed prefix) and group 2 (the optional suffix)
        return (match.group(1) + match.group(2)).replace(" ", "")
    return input_string.replace(" ", "")





def renombrar_expediente(carpeta_origen, carpeta_id, conversion_dict):
    id = carpeta_id
    for nom_archivo in os.listdir(carpeta_origen):
        if nom_archivo.endswith(".pdf"):
            nombre_base = os.path.splitext(nom_archivo)[0]
            if nombre_base == id:
                nuevo_nombre = f"{id}-{conversion_dict['empty']}.pdf"
            else:
                nombre_base = transform_pd_code(nombre_base)
                nuevo_nombre = f"{id}-{conversion_dict[nombre_base]}.pdf"
            ruta_archivo_viejo = os.path.join(carpeta_origen, nom_archivo)
            ruta_archivo_nuevo = os.path.join(carpeta_origen, nuevo_nombre)
            os.rename(ruta_archivo_viejo, ruta_archivo_nuevo)
            print(f"Renamed {ruta_archivo_viejo} to {ruta_archivo_nuevo}")

def renombrar_archivos_en_carpeta(carpeta_origen, carpeta_id, conversion_dict):
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
    renombrar_expediente(carpeta_origen, carpeta_id, conversion_dict)

def renombrar_archivos_en_rango(carpeta_mes, intervalo_inicial, intervalo_final, conversion_dict):
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
            renombrar_archivos_en_carpeta(carpeta_origen, i, conversion_dict)
        else:
            print(f"Folder {carpeta_origen} does not exist. Skipping.")
