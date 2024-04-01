from tkinter import *
class Interface:
    def __init__(self,contenedor):
        self.e1=Label(contenedor, text='etiqueta1',fg='blue',bg='red')
        self.e2=Label(contenedor, text='etiqueta2',fg='black',bg='orange')
        self.e3=Label(contenedor, text='etiqueta1',fg='white',bg='black')
        self.e4=Label(contenedor, text='etiqueta4',fg='blue',bg='red')
        self.e5=Label(contenedor, text='etiqueta5',fg='black',bg='orange')
        self.e6=Label(contenedor, text='etiqueta6',fg='white',bg='black')
        
        self.e1.grid(column=0,row=0)
        self.e2.grid(column=0,row=1)
        self.e3.grid(column=0,row=2)
        self.e4.grid(column=1,row=0)
        self.e5.grid(column=1,row=1)
        self.e6.grid(column=1,row=2)
ventana=Tk()
i1=Interface(ventana)
ventana.mainloop()