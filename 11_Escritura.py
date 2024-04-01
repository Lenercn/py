def escritura(datoa,datob,datoc):
    prueba=open('datos.txt','w')
    prueba.write(datoa)
    prueba.write(datob)
    prueba.write(datoc)
    print('/n escritura /n')
    prueba.close
escritura('mundo ','bello ','bonito ')

def lectura():
    prueba=open('datos.txt','r')
    print(prueba.read())
    prueba.close
lectura()