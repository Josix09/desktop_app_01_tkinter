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

#-------------------------------
#Frame_1
#-------------------------------
frame_1 = Frame(Ventana_principal)
frame_1.config(bg="yellow",width=780, height=250)
frame_1.place(x=10,y=10)
#-------------------------------
#Frame 2
#-------------------------------
frame_2 = Frame(Ventana_principal)
frame_2.config(bg="blue",width=780, height=120)
frame_2.place(x=10,y=250)
#-------------------------------
#Bandera
#-------------------------------
frame_3 = Frame(Ventana_principal)
frame_3.config(bg="red",width=780, height=120)
frame_3.place(x=10,y=370)



#metodo principal que despliega la ventana en pantalla
Ventana_principal.mainloop()

