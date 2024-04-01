from tkinter import *
class Color:
    def __init__(self,contenedor):
        self.txtColor=Label(contenedor,text='Selecionar color',fg='black',bg='white')
        self.c1=Button(contenedor, text='AMARILLO', fg='black',bg='yellow',command=self.amarillo)
        self.c2=Button(contenedor, text='ROJO', fg='white',bg='red',command=self.rojo)
        self.c3=Button(contenedor, text='Celeste', fg='black',bg='cyan',command=self.blanco)


        self.txtColor.grid(column=0,row=0,columnspan=3)
        self.c1.grid(column=0,row=1)
        self.c2.grid(column=1,row=1)
        self.c3.grid(column=2,row=1)

    def amarillo(self):
        self.txtColor.config(fg='black',bg='yellow')
    def rojo(self):
        self.txtColor.config(fg='white',bg='red' )
    def blanco(self):
        self.txtColor.config(fg='black',bg='cyan' )

        # if self ['text']=='ROJO':
        #     
        # if self ['text']=='BLANCO':
        #     self.txtColor.config(fg='white',bg='black' )
        




ventana=Tk()
i1=Color(ventana)
ventana.mainloop()