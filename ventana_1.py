# se importa la libreria tkinter con todas sus funciones
from tkinter import *

#------------------------------
# Funciones de la app
#------------------------------


#------------------------------
# Ventana principal de la app
#------------------------------

# se declara una variable llamada ventana principal que adquiere las características de un objeto tipo Tk()

Ventana_principal = Tk()

#Titulo de la ventana

Ventana_principal.title("Jorge Luis Silva Morales")

#tamaño de la ventana
Ventana_principal.geometry("800x500")

#Deshabilitar el botón de maximizar de la ventana
Ventana_principal.resizable(0,0)

#color de fondo de la ventana

Ventana_principal.config(bg="green")

#metodo principal que despliega la ventana en pantalla
Ventana_principal.mainloop()

