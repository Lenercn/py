class Persona:
    def __init__(self,edad, nombre):
        self.edad=edad
        self.nombre=nombre
        print ('se ha creado a ', self.nombre,' y tiene ', self.edad, ' años')
# el * * se usas para decir que le pasaremos una diccionario
    def hablar(self,**palabras):
        for frase in palabras:
            print(self.nombre,':',palabras[frase])
    
juan=Persona(18,'juan')
juan.hablar(t1='hola  mundo',t2='soy yo',t3= 'pun perro', t4='xdddddd')