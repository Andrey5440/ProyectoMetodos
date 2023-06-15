from tkinter import Tk, Label, Entry, Button
import pulp as plp

# Crear una función para resolver el problema de programación lineal
def solve_linear_programming_problem():
    x_value = float(entry.get())

    # Crear el problema de programación lineal
    problem = plp.LpProblem("Problema de Programación Lineal", plp.LpMaximize)

    # Definir la variable de decisión
    x = plp.LpVariable("x", lowBound=0)  # Variable x >= 0

    # Definir la función objetivo
    problem += x

    # Definir la restricción
    problem += x <= x_value

    # Resolver el problema
    problem.solve()

    # Obtener el resultado
    optimal_value = plp.value(x)

    # Actualizar la etiqueta con el valor óptimo
    label["text"] = "Valor óptimo de x: {}".format(optimal_value)

# Crear la ventana principal
root = Tk()
root.title("Programación Lineal")

# Crear los widgets de la interfaz
label = Label(root, text="")
label.pack(pady=10)

entry = Entry(root)
entry.pack(pady=10)

button = Button(root, text="Resolver", command=solve_linear_programming_problem)
button.pack(pady=10)

# Ejecutar el bucle de eventos
root.mainloop()