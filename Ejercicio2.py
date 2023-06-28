import tkinter as tk
from tkinter import messagebox
from queue import Queue

class QueueProgram:
    def __init__(self):
        self.queue = Queue()
        self.window = tk.Tk()
        self.window.title("Programa de Colas")
        
        self.label = tk.Label(self.window, text="Ingrese los elementos a la cola:")
        self.label.pack()
        
        self.entry = tk.Entry(self.window)
        self.entry.pack()
        
        self.add_button = tk.Button(self.window, text="Agregar a la cola", command=self.enqueue)
        self.add_button.pack()
        
        self.remove_button = tk.Button(self.window, text="Remover de la cola", command=self.dequeue)
        self.remove_button.pack()
        
        self.empty_button = tk.Button(self.window, text="Verificar si está vacía", command=self.is_empty)
        self.empty_button.pack()
        
        self.size_button = tk.Button(self.window, text="Ver tamaño de la cola", command=self.get_size)
        self.size_button.pack()
        
        self.window.mainloop()
    
    def enqueue(self):
        try:
            element = int(self.entry.get())
            self.queue.put(element)
            self.entry.delete(0, tk.END)
            messagebox.showinfo("Éxito", "El elemento se ha agregado a la cola.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número entero válido.")
    
    def dequeue(self):
        if not self.queue.empty():
            element = self.queue.get()
            messagebox.showinfo("Elemento Removido", f"El elemento {element} ha sido removido de la cola.")
        else:
            messagebox.showwarning("Cola Vacía", "La cola está vacía.")
    
    def is_empty(self):
        if self.queue.empty():
            messagebox.showinfo("Cola Vacía", "La cola está vacía.")
        else:
            messagebox.showinfo("Cola no Vacía", "La cola no está vacía.")
    
    def get_size(self):
        size = self.queue.qsize()
        messagebox.showinfo("Tamaño de la Cola", f"El tamaño de la cola es: {size}.")

queue_program = QueueProgram()
