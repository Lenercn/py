import sqlite3

# conexion=sqlite3.connect('musica.db')
# consulta=conexion.cursor()
# tabla="create table tabla(id integer primary key autoincrement not null, cancion varchar(30), artista varchar(20), album varchar(15) not null);"
# print(tabla)
# if (consulta.execute(tabla)):
#     print('tabla creada')
# else:
#     print('F, NO SE CREO')
# consulta.close()
# conexion.commit()
# conexion.close





def insertar():
    db1=sqlite3.connect('musica.db')
    print('Funcion insertar')
    cancion=str(input('Nombre de la cancion: '))
    artista=str(input('Artista: '))
    album=str(input('Album: '))
    
    
    consulta=db1.cursor()

    strConsulta = "insert into tabla(cancion,artista,album) values('" + cancion + "','" + artista + "','" + album + "')"

    print(strConsulta)

    consulta.execute(strConsulta)
    consulta.close()
    db1.commit()
    db1.close()
def consultar():
    db2=sqlite3.connect('musica.db')
    print('vamos a consultar')
    db2.row_factory=sqlite3.Row
    consulta=db2.cursor()
    consulta.execute("select * from tabla")
    filas=consulta.fetchall()
    lista=[]
    for fila in filas:
        s={}
        s['id']=fila['id']
        s['cancion']=fila['cancion']
        s['artista']=fila['artista']
        s['album']=fila['album']
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
        listacanciones=consultar()
        for cancion in listacanciones:
            print(cancion['id'],cancion['cancion'], cancion['artista'], cancion['album'])
        menu()
    elif opc==3:
        exit()
menu()