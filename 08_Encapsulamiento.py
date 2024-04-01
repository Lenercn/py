
class Persona:
    def __init__(self,edad,nombre):
        self.edad=edad
        self.nombre=nombre
        print ('se ha creado a ', self.nombre,' y tiene ', self.edad, ' años')

    def hablar(self,palabras):

        print(self.nombre,':',palabras)

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
    
juan=Persona(18,'juan')
juan.hablar('Viva el apra')

luis=deportista(25,'luis','fut')
luis.practicarDeporte()
#Llamando al atributo encapsulado
print('luis practica',luis.verMiDeporte())