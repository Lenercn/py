from tkinter import *
class Interface:
    def __init__(self,contenedor):
        self.e1=Label(contenedor, text='etiqueta1',fg='blue',bg='red')

        self.e1.pack()
ventana=Tk()
i1=Interface(ventana)
ventana.mainloop()