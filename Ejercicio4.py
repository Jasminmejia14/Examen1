import tkinter as tk
from tkinter import messagebox

class ArrayProgram:
    def __init__(self):
        self.array = []
        self.window = tk.Tk()
        self.window.title("Programa de Arreglos")
        
        self.label = tk.Label(self.window, text="Ingrese los elementos al arreglo:")
        self.label.pack()
        
        self.entry = tk.Entry(self.window)
        self.entry.pack()
        
        self.add_button = tk.Button(self.window, text="Agregar al arreglo", command=self.add_element)
        self.add_button.pack()
        
        self.sort_button = tk.Button(self.window, text="Ordenar de menor a mayor", command=self.bubble_sort)
        self.sort_button.pack()
        
        self.size_button = tk.Button(self.window, text="Tamaño del arreglo", command=self.get_size)
        self.size_button.pack()
        
        self.max_element_button = tk.Button(self.window, text="Elemento de mayor valor", command=self.get_max_element)
        self.max_element_button.pack()
        
        self.min_element_button = tk.Button(self.window, text="Elemento de menor valor", command=self.get_min_element)
        self.min_element_button.pack()
        
        self.window.mainloop()
    
    def add_element(self):
        try:
            element = int(self.entry.get())
            if element == 0:
                self.entry.delete(0, tk.END)
                messagebox.showinfo("Fin del ingreso", "Ingreso de datos finalizado.")
            else:
                self.array.append(element)
                self.entry.delete(0, tk.END)
                messagebox.showinfo("Éxito", "El elemento se ha agregado al arreglo.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número entero válido.")
    
    def bubble_sort(self):
        n = len(self.array)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
        messagebox.showinfo("Ordenamiento", "El arreglo ha sido ordenado de menor a mayor.")
    
    def get_size(self):
        size = len(self.array)
        messagebox.showinfo("Tamaño del Arreglo", f"El tamaño del arreglo es: {size}.")
    
    def get_max_element(self):
        if len(self.array) > 0:
            max_element = max(self.array)
            messagebox.showinfo("Elemento de Mayor Valor", f"El elemento de mayor valor es: {max_element}.")
        else:
            messagebox.showwarning("Arreglo Vacío", "El arreglo está vacío.")
    
    def get_min_element(self):
        if len(self.array) > 0:
            min_element = min(self.array)
            messagebox.showinfo("Elemento de Menor Valor", f"El elemento de menor valor es: {min_element}.")
        else:
            messagebox.showwarning("Arreglo Vacío", "El arreglo está vacío.")

array_program = ArrayProgram()
