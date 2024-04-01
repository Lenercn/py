class Persona:
    def __init__(self,edad, nombre):
        self.edad=edad
        self.nombre=nombre
        print ('se ha creado a ', self.nombre,' y tiene ', self.edad, ' años')
# el * se usas para decir que le pasaremos una tupla
    def hablar(self,*palabras):
        for frase in palabras:
            print(self.nombre,':',frase)
    
juan=Persona(18,'juan')
juan.hablar('hola  mundo','soy yo', 'pun perro', 'xdddddd')