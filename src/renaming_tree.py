import os
import sys
import treenodepersonal

def sort_key(s):
    # Split the string at the hyphen
    first_part = s.split('-')[0]
    # Convert the first part to an integer
    return int(first_part)

# Rename files in a folder based on the tree
def find_keys(folder_path):
    keys = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            base_name = os.path.splitext(file_name)[0]
            keys.append(base_name.split("merged-")[-1])  # Extract the key part from the filename
            #
            keys = sorted(keys, key=sort_key)
    return keys

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
        

def main():
    if len(sys.argv) != 4:
        print("Usage: python rename_pdfs.py <month_folder> <start_interval> <end_interval>")
        sys.exit(1)

    month_folder = sys.argv[1]
    start_interval = int(sys.argv[2])
    end_interval = int(sys.argv[3])

    # Check if the month folder exists
    if not os.path.isdir(month_folder):
        print("The specified month folder does not exist.")
        sys.exit(1)

    # Build the renaming rules tree
    renaming_tree = treenodepersonal.build_renaming_tree()

    # Iterate through each folder within the specified interval in the month folder
    for i in range(start_interval, end_interval + 1):
        folder_path = os.path.join(month_folder, str(i))

        # Check if the folder exists
        if os.path.isdir(folder_path):
            rename_files_in_folder(folder_path, i, renaming_tree)
        else:
            print(f"Folder {folder_path} does not exist. Skipping.")

if __name__ == "__main__":
    main()
