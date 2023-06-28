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
        
        self.sort_button = tk.Button(self.window, text="Ordenar de mayor a menor", command=self.selection_sort)
        self.sort_button.pack()
        
        self.size_button = tk.Button(self.window, text="Tamaño del arreglo", command=self.get_size)
        self.size_button.pack()
        
        self.average_button = tk.Button(self.window, text="Promedio del arreglo", command=self.get_average)
        self.average_button.pack()
        
        self.sum_button = tk.Button(self.window, text="Suma de los elementos", command=self.get_sum)
        self.sum_button.pack()
        
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
    
    def selection_sort(self):
        n = len(self.array)
        for i in range(n - 1):
            max_idx = i
            for j in range(i + 1, n):
                if self.array[j] > self.array[max_idx]:
                    max_idx = j
            self.array[i], self.array[max_idx] = self.array[max_idx], self.array[i]
        messagebox.showinfo("Ordenamiento", "El arreglo ha sido ordenado de mayor a menor.")
    
    def get_size(self):
        size = len(self.array)
        messagebox.showinfo("Tamaño del Arreglo", f"El tamaño del arreglo es: {size}.")
    
    def get_average(self):
        if len(self.array) > 0:
            average = sum(self.array) / len(self.array)
            messagebox.showinfo("Promedio del Arreglo", f"El promedio del arreglo es: {average:.2f}.")
        else:
            messagebox.showwarning("Arreglo Vacío", "El arreglo está vacío.")
    
    def get_sum(self):
        total_sum = sum(self.array)
        messagebox.showinfo("Suma de los Elementos", f"La suma de los elementos del arreglo es: {total_sum}.")

array_program = ArrayProgram()
