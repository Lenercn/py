# class automovil:
#     #atributos
#     def __init__(self, color, modelo, marca):
#         self.color=color
#         self.modelo=modelo
#         self.marca=marca
#     #metodos
#     def correr(self, *velocidad ):
#             print('El automovil ', self.marca,self.modelo,self.color,'tiene una velocidad de: ',velocidad)

# c1=automovil('rojo','fotuner','toyota')
# c1.correr('15 km/h','25km')


class escuela:
    def __init__(self,numero, localidad, distrito) :
          self.numero=numero
          self.localidad=localidad
          self.distrito=distrito


    def  maestro(self,**datos):
        for xx in datos:
            print(datos[xx],'pertenece a ', self.numero, self.localidad, self.distrito)
    
maestros=escuela('202222','sapuc','asuncion')
maestros.maestro(m1='juan',m2='luis')
