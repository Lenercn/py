import sqlite3

def insertar():
    db1=sqlite3.connect('novelas.db')
    print('Funcion insertar')

    nombre1=str(input('Nombre de novela: '))
    autor1=str(input('Autor: '))
    year1=str(input('Año de publicacion: '))

    consulta=db1.cursor()

    strConsulta = "insert into tabla(nombre,autor,year) values('" + nombre1 + "','" + autor1 + "','" + year1 + "')"

    print(strConsulta)


    consulta.execute(strConsulta)
    consulta.close()
    db1.commit()
    db1.close()


def consultar():
    db2=sqlite3.connect('novelas.db')
    print('vamos a consultar')
    db2.row_factory=sqlite3.Row
    consulta=db2.cursor()
    consulta.execute("select * from tabla")
    filas=consulta.fetchall()
    lista=[]
    for fila in filas:
        s={}
        s['nombre']=fila['nombre']
        s['autor']=fila['autor']
        s['year']=fila['year']
        lista.append(s)
    consulta.close()
    db2.close()
    return(lista)

def menu():
    opc=int (input("\n **Menu**\n 1.Insertar \n 2.Consultar \n 3.Salir\n opc: "))
    if opc==1:
        insertar()
        menu()
    elif opc==2:
        listaNovelas=consultar()
        for novela in listaNovelas:
            print(novela['nombre'], novela['autor'], novela['year'])
        menu()
    elif opc==3:
        exit()
menu()




