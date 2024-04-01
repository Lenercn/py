def menu():
    opc=int(input("\n **Menu**\n 1.if \n 2.Anidado \n 3.Repeticion \n 8.Salir\n opc: "))
    if opc==1:
        simple()
        menu()
    elif opc==2:
        anidados()
        menu()
    elif opc==3:
        repeticion()
        menu()
    elif opc==8:
        exit()

        
def simple():
    pregunta=int(input('Cuantos libros lees? \n'))
    if pregunta>10:
        msj='buen lector'
     
    else:
       msj= 'animo tu puedes'
    print(msj)

def anidados():
    pregunta=str.upper( input('trabajas desde casa ?: '))

    if pregunta=='SI':
        msj='afortunado'
    if pregunta=='NO':
        msj='f, por ti'
        tiempo=int(input('a cuanto tiempo esta tu trabajo?: '))
        if tiempo> 30:
            msj2='que lejos vives'
        else:
            msj2='esta cerca'
        print(msj2)
    print(msj)
def repeticion():
    def mini():
        op=int(input('\n mini menu \n 1. While \n 2. For \n 3. volver \n'))
        if op==1:
            multiplicador=int(input('Ingrese cantidad de Multiplicandos:'))
            i=0
            while i<=multiplicador:
                print('7 X ',i,'=',7*i)
                i+=1
        elif op==2:
            multiplicando=int(input('Multiplicando: \n'))
            multiplicador=int(input('Ingrese cantidad de Multiplicandos:\n'))
            i=0
            for i in range(multiplicador+1):
                print(multiplicando,' X ',i,'=',i*multiplicando)
                i+=1
        elif op==3:
            menu()
    mini()

    
menu()
