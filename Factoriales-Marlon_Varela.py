import tkinter as tk
from tkinter import messagebox


def factorial_iterativa(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def factorial_recursiva(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursiva(n - 1)


def calcular_factorial():
    try:
        n = int(entry1.get())
        result_iterativa = factorial_iterativa(n)
        result_recursiva = factorial_recursiva(n)
        messagebox.showinfo("Resultado", f"Factorial (Iterativa): {result_iterativa}\n"
                                       f"Factorial (Recursiva): {result_recursiva}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un numero entero.")


window = tk.Tk()
window.title("Factorial de un numero por Iteracion y Recursiva con TKinter - Marlon Varela")
window.geometry("600x200")

label1 = tk.Label(window, text="Ingrese un numero:")
label1.pack()

entry1 = tk.Entry(window)
entry1.pack()

labelinv = tk.Label(window, text=" ")
labelinv.pack() #Solo puse este label para crear un espacio

button1 = tk.Button(window, text="Calcular", command=calcular_factorial)
button1.pack()

window.mainloop()

