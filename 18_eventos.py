from tkinter import *
class Interface:
    def __init__(self,contenedor):
        self.textoE3=StringVar()
        self.e1=Label(contenedor, text='Convertir celsius a farenheit',fg='black')
        self.e2=Label(contenedor, text='celsius',fg='black')
        self.e3=Label(contenedor, text='farenheit',fg='black')
        self.e4=Button(contenedor, text='Convertir',fg='blue',bg='cyan', command=self.convertir)
        self.e5=Entry (contenedor,fg='black',bg='orange')
        self.e6=Label(contenedor,fg='white',bg='black', textvariable=self.textoE3)

        
        self.e1.grid(column=0,row=0, columnspan=2)
        self.e2.grid(column=0,row=1)
        self.e3.grid(column=0,row=2)
        self.e4.grid(column=0,row=3, columnspan=2)

        self.e5.grid(column=1,row=1)
        self.e6.grid(column=1,row=2)
    def convertir(self):
        cel=float(self.e5.get())
        far=(cel*1.8)+32
        self.textoE3.set(far)


ventana=Tk()
i1=Interface(ventana)
ventana.mainloop()