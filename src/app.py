import renaming_tree 
import treenodepersonal 
import os 
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import re  # Add this import for regular expressions

def transform_pd_code(input_string):
    """
    Transform strings like 'PD2650-1' to 'PD-1'
    
    Args:
        input_string (str): The string to transform (e.g., 'PD2650-1')
        
    Returns:
        str: The transformed string (e.g., 'PD-1') or the original string if the pattern doesn't match
    """
    if not input_string:
        return input_string
    
    # Pattern to match: "PD" followed by digits, then "-" and more characters
    pattern = r'(PD)(\d+)(-\w+)'
    match = re.match(pattern, input_string)
    
    if match:
        pd_prefix = match.group(1)  # "PD"
        suffix = match.group(3)     # "-1"
        return pd_prefix + suffix   # "PD-1"
    
    return input_string  # Return original if pattern doesn't match

class AyudaScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ayuda Scanner")
        self.root.geometry("800x600")
        
        # Set up the main container frame
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Directory selection
        dir_frame = ttk.LabelFrame(self.main_frame, text="Selecciona la carpeta")
        dir_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.dir_path = tk.StringVar()
        ttk.Entry(dir_frame, textvariable=self.dir_path, width=70).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(dir_frame, text="Busca", command=self.browse_directory).pack(side=tk.LEFT, padx=5, pady=5)
        
        # Operation frame
        op_frame = ttk.LabelFrame(self.main_frame, text="Operaciones")
        op_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(op_frame, text="Cambiar nombres", command=self.scan_directory).pack(side=tk.LEFT, padx=5, pady=5)
        
        # Results frame
        results_frame = ttk.LabelFrame(self.main_frame, text="Resultados")
        results_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # OJO CON ESTO Treeview for file hierarchy display
        self.tree_view = ttk.Treeview(results_frame)
        self.tree_view.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.tree_view.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree_view.configure(yscrollcommand=scrollbar.set)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Listo")
        status_bar = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Store the renaming tree instance
        self.rename_tree = None
        
    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.dir_path.set(directory)
            self.status_var.set(f"Seleccionar Carpeta: {directory}")
    
    def scan_directory(self):
        directory = self.dir_path.get()
        if not directory:
            messagebox.showwarning("Cuidado", "Selecciona una carpeta primero.")
            return
        
        try:
            self.status_var.set("Escaneando Carpeta...")
            self.root.update()
            
            # Clear the treeview
            for item in self.tree_view.get_children():
                self.tree_view.delete(item)
            
            # Create a renaming tree object
            self.rename_tree = renaming_tree.RenamingTree(directory)
            
            # Populate treeview with current directory structure
            self._populate_tree(self.rename_tree.root, '')
            
            self.status_var.set(f"Carpeta Escaneada: {directory}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al Escanear Carpeta: {str(e)}")
            self.status_var.set("Error escaneando carpeta")
    

 
def main():
    root = tk.Tk()
    app = AyudaScannerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

