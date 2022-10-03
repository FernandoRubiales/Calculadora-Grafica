# CALCULADORA - PROYECTO N°4

# Del módulo Tkinter importamos todo
from tkinter import *

# Definimos la variable

root = Tk()

# Agregamos, titulo e icono
root.title("CALCULADORA GRÁFICA")
root.iconbitmap("Calculator_30001.ico")

# Entrada
entrada_texto = Entry(root, font="Calibri 20")
entrada_texto.grid(row = 0, column= 0, columnspan= 4, padx=5, pady=5)

# Creamos las Funciones
indice = 0

def click_boton(valor):
    global indice
    entrada_texto.insert(indice,valor)
    indice += 1 

def borrar():
    entrada_texto.delete(0,END)
    indice = 0

def operacion():
    ecuacion = entrada_texto.get()
    resultado = eval(ecuacion)
    entrada_texto.delete(0,END)
    entrada_texto.insert(0,resultado)
    indice = 0


# Creamos los Botones
boton1 = Button(root, text= "1", width=5, height=2, command= lambda: click_boton(1))
boton2 = Button(root, text= "2", width=5, height=2, command= lambda: click_boton(2))
boton3 = Button(root, text= "3", width=5, height=2, command= lambda: click_boton(3))
boton4 = Button(root, text= "4", width=5, height=2, command= lambda: click_boton(4))
boton5 = Button(root, text= "5", width=5, height=2, command= lambda: click_boton(5))
boton6 = Button(root, text= "6", width=5, height=2, command= lambda: click_boton(6))
boton7 = Button(root, text= "7", width=5, height=2, command= lambda: click_boton(7))
boton8 = Button(root, text= "8", width=5, height=2, command= lambda: click_boton(8))
boton9 = Button(root, text= "9", width=5, height=2, command= lambda: click_boton(9))
boton0 = Button(root, text= "0", width=14, height=2, command= lambda: click_boton(0))

boton_borrar = Button(root, text= "AC", width=5, height=2, command= lambda: borrar())
boton_parentesis1 = Button(root, text= "(", width=5, height=2, command= lambda: click_boton("("))
boton_parentesis2 = Button(root, text= ")", width=5, height=2, command= lambda: click_boton(")"))
boton_punto= Button(root, text= ".", width=5, height=2, command= lambda: click_boton("."))

boton_división = Button(root, text= "/", width=5, height=2, command= lambda: click_boton("/"))
boton1_multiplicación= Button(root, text= "x", width=5, height=2, command= lambda: click_boton("*"))
boton_resta = Button(root, text= "-", width=5, height=2, command= lambda: click_boton("-"))
boton_suma = Button(root, text= "+", width=5, height=2, command= lambda: click_boton("+"))
boton_igual = Button(root, text= "=", width=5, height=2, command= lambda: operacion())

# Agregamos botones en pantalla
boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_división.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton1_multiplicación.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_resta.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_suma.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
boton_punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)

root.mainloop()