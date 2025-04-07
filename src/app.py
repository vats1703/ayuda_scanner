import os
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from renaming_version2 import renombrar_archivos_en_rango

class TextRedirector(object):
    def __init__(self, widget):
        self.widget = widget

    def write(self, str_text):
        self.widget.config(state=tk.NORMAL)
        self.widget.insert(tk.END, str_text)
        self.widget.see(tk.END)
        self.widget.config(state=tk.DISABLED)

    def flush(self):
        pass

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        # Update folder entry
        folder_entry.config(state="normal")
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder)
        folder_entry.config(state="readonly")
        
        # Clear the log text widget
        log_text.config(state=tk.NORMAL)
        log_text.delete("1.0", tk.END)
        log_text.config(state=tk.DISABLED)

def run_renaming():
    folder = folder_entry.get()
    try:
        intervalo_inicial = int(start_entry.get())
        intervalo_final = int(end_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un intervalo numérico válido.")
        return

    if not os.path.isdir(folder):
        messagebox.showerror("Error", "La carpeta seleccionada no es valida.")
        return

    # Redirect stdout to the log_text widget
    old_stdout = sys.stdout
    sys.stdout = TextRedirector(log_text)
    
    try:
        renombrar_archivos_en_rango(folder, intervalo_inicial, intervalo_final)
        messagebox.showinfo("Success", "Archivos renombrados satisfactoriamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Un error ha ocurrido: {e}")
    finally:
        sys.stdout = old_stdout

# --- Setup UI ---
root = tk.Tk()
root.title("Renombrar Archivos")
root.geometry("800x500")

frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

# Folder selection
folder_label = ttk.Label(frame, text="Carpeta Mes:")
folder_label.grid(row=0, column=0, sticky=tk.W, pady=(0,5))
folder_entry = ttk.Entry(frame, width=40, state="readonly")
folder_entry.grid(row=0, column=1, padx=5, pady=(0,5))
browse_btn = ttk.Button(frame, text="Browse", command=browse_folder)
browse_btn.grid(row=0, column=2, padx=5, pady=(0,5))

# Intervalo Inicio
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
run_btn = ttk.Button(frame, text="Renombrar Expedientes", command=run_renaming)
run_btn.grid(row=3, column=1, pady=10)

# Log display area
log_label = ttk.Label(frame, text="Información sobre archivos:")
log_label.grid(row=4, column=0, sticky=tk.W, pady=(10,0))
log_text = tk.Text(frame, height=10, width=100, state=tk.DISABLED)
log_text.grid(row=5, column=0, columnspan=3, pady=(0,10))

root.mainloop()