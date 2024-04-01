class Persona:
    def __init__(self):
        self.edad=18
        self.nombre='juan'
        print ('se ha creado a ', self.nombre,' y tiene ', self.edad, ' años')

    def hablar(self,palabras='pum perro'):

        print(self.nombre,':',palabras)
    
juan=Persona()
juan.hablar()
juan.hablar('xddd')