from abc import ABCMeta, abstractmethod
class Persona:

    __metaclass__=ABCMeta

    def __init__(self,edad,nombre):
        self.edad=edad
        self.nombre=nombre
        print ('se ha creado a ', self.nombre,' y tiene ', self.edad, ' años')


    @abstractmethod
    def hablar(self):pass

# declarando depeoritsta que herada de persona

class deportista(Persona):
    def __init__(self, edad, nombre, deporte):
        self.edad=edad
        self.nombre=nombre
        #encapsulando deporte
        self.__deporte=deporte
        print ('se ha creado a ', self.nombre,' y tiene ', self.edad, ' años')


    def practicarDeporte(self):
        print(self.nombre, ': voy a practicar')

    #acceder al atrinuto encapsulado
    def verMiDeporte(self):
        return self.__deporte
    
    def hablar(self,*palabras):
        for frase in palabras:
            print(self.nombre,frase)
#una clase derivada de una clase abstracta se denomina implementacion
#   
    

luis=deportista(25,'luis','fut')
luis.hablar('VIVA EL APRA', 'El apra nunca muere')
luis.practicarDeporte()
#Llamando al atributo encapsulado
print('luis practica',luis.verMiDeporte())