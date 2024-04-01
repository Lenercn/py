# class figura:
#     def __init__(self, base, altura) :
#         self.base=base
#         self.altura=altura

#         print((self.base*self.altura)/2)
# triangulo=figura(10,5)

# import random
# class Dado:

#     def __init__(self,veces):
#         self.veces=veces
#         i=1
#         lan=0
#         suma=0
#         uno,dos,tres,cuatro,cinco,seis=0,0,0,0,0,0
#         dos=0
#         while i <=veces:
#             i=i+1
#             lan=random.randint(1,6)
#             suma=suma+lan
#             if lan==1:
#                uno=1+uno
#             if lan==2:
#                dos=1+dos
  
            
#             print('D',i,' es: ', lan,' Suma: ')
#         print('La suma es: ',suma)
#         print('salio\n unos:',uno,'\n Dos:',dos)

# l=random.randint(1,100)
# lanzar=Dado(l)


# #sobre escritura
# class boligrafo:
#     def __init__(self, marca,color):
#         self.marca=marca
#         self.color=color
#         print('Boligrafo: ', self.marca, self.color)


# class tinta(boligrafo):
#     def __init__(self, marca, color,tinta):
#         self.marca=marca
#         self.color=color
#         self.tinta=tinta
#         print('Tipo de tinta:', self.tinta)



# pen=boligrafo('stabilo', 'negro')
# pen2=tinta('pilot', 'azul','liquida')
# pen2.tinta


class animal:
    def __init__(self, especie, nombre):
        self.especie=especie
        self.nombre=nombre
        print('Mi especie es: ',self.especie,'me llaman: ',self.nombre)
    def hablar(self,palabra):
        self.palabra=palabra
        print('Estoy hablando: ', self.palabra)

conejo=animal('conejino','Conejo')
conejo.hablar('OHHH perro')
print(conejo.__dict__)