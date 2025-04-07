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




def rename_files_in_folder(folder_path, folder_id, renaming_tree):
    keys = find_keys(folder_path)
    keys_bm = keys[0]
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            base_name = os.path.splitext(file_name)[0]
            key = base_name.split("merged-")[-1]  # Extract the key part from the filename 
            if keys_bm == '1-2':
                if key == keys_bm:
                    new_value = renaming_tree.find_value(key)
                else:
                    new_value = renaming_tree.children['1-2'].find_value(key)

            elif keys_bm == '1-6':
                if key == keys_bm:
                    new_value = renaming_tree.find_value(key)
                else:
                    new_value = renaming_tree.children['1-6'].find_value(key)

            else:
                new_value = None
                
            if new_value:
                new_name = f"{folder_id}-{new_value}.pdf"
                old_file_path = os.path.join(folder_path, file_name)
                new_file_path = os.path.join(folder_path, new_name)
                os.rename(old_file_path, new_file_path)
                print(f"Renamed {old_file_path} to {new_file_path}")
            else:
                print(f"No matching rule for {file_name}, leaving it unchanged.")
        

# def main():
#     if len(sys.argv) != 4:
#         print("Usage: python rename_pdfs.py <month_folder> <start_interval> <end_interval>")
#         sys.exit(1)

#     month_folder = sys.argv[1]
#     start_interval = int(sys.argv[2])
#     end_interval = int(sys.argv[3])

#     # Check if the month folder exists
#     if not os.path.isdir(month_folder):
#         print("The specified month folder does not exist.")
#         sys.exit(1)

#     # Build the renaming rules tree
#     renaming_tree = treenodepersonal.build_renaming_tree()

#     # Iterate through each folder within the specified interval in the month folder
#     for i in range(start_interval, end_interval + 1):
#         folder_path = os.path.join(month_folder, str(i))

#         # Check if the folder exists
#         if os.path.isdir(folder_path):
#             rename_files_in_folder(folder_path, i, renaming_tree)
#         else:
#             print(f"Folder {folder_path} does not exist. Skipping.")

# if __name__ == "__main__":
#     main()
