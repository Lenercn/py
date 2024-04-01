class Persona:
    def __init__(self,edad,nombre):
        self.edad=edad
        self.nombre=nombre
        print ('se ha creado a ', self.nombre,' y tiene ', self.edad, ' años')

    def hablar(self,palabras):

        print(self.nombre,':',palabras)
    
juan=Persona(18,'juan')
juan.hablar('Viva el apra')

luis=Persona(25,'luis')
luis.hablar('me dicen lucho')