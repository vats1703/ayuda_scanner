import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from renaming_version2 import renombrar_archivos_en_rango, conversion_dict

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder)

def run_renaming():
    folder = folder_entry.get()
    try:
        intervalo_inicial = int(start_entry.get())
        intervalo_final = int(end_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for the interval.")
        return
    
    if not os.path.isdir(folder):
        messagebox.showerror("Error", "The selected folder is not a valid directory.")
        return

    try:
        renombrar_archivos_en_rango(folder, intervalo_inicial, intervalo_final, conversion_dict)
        messagebox.showinfo("Success", "Files renamed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# --- Setup UI ---
root = tk.Tk()
root.title("Renombrar Archivos")
root.geometry("400x200")

frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

# Folder selection
folder_label = ttk.Label(frame, text="Carpeta Mes:")
folder_label.grid(row=0, column=0, sticky=tk.W, pady=(0,5))
folder_entry = ttk.Entry(frame, width=40)
folder_entry.grid(row=0, column=1, padx=5, pady=(0,5))
browse_btn = ttk.Button(frame, text="Browse", command=browse_folder)
browse_btn.grid(row=0, column=2, padx=5, pady=(0,5))

# Intervalo Inicia
start_label = ttk.Label(frame, text="Intervalo Inicio:")
start_label.grid(row=1, column=0, sticky=tk.W, pady=5)
start_entry = ttk.Entry(frame, width=10)
start_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

# Intervalo Final
end_label = ttk.Label(frame, text="Intervalo Final:")
end_label.grid(row=2, column=0, sticky=tk.W, pady=5)
end_entry = ttk.Entry(frame, width=10)
end_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

# Run button
run_btn = ttk.Button(frame, text="Renombrar Archivos", command=run_renaming)
run_btn.grid(row=3, column=1, pady=10)

root.mainloop()