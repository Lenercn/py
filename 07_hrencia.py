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
        self.deporte=deporte
        print ('se ha creado a ', self.nombre,' y tiene ', self.edad, ' años')


    def practicarDeporte(self):
        print(self.nombre, ': voy a practicar')
    
juan=Persona(18,'juan')
juan.hablar('Viva el apra')

luis=deportista(25,'luis','fut')
luis.practicarDeporte()
print('luis practica',luis.deporte)