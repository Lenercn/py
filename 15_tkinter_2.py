from tkinter import *
class Interface:
    def __init__(self,contenedor):
        self.e1=Label(contenedor, text='etiqueta1',fg='blue',bg='red')
        self.e2=Label(contenedor, text='etiqueta2',fg='black',bg='orange')
        self.e3=Label(contenedor, text='etiqueta1',fg='white',bg='black')

        self.e1.pack(side=TOP)
        self.e2.pack(side=RIGHT)
        self.e3.pack(side=BOTTOM, fill=X)
ventana=Tk()
i1=Interface(ventana)
ventana.mainloop()