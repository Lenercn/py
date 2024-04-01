import sqlite3
def consultar():
    db2=sqlite3.connect('novelas.db')
    # print('vamos a consultar')
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

listaNovelas=consultar()
# for novela in listaNovelas:
#     print(novela['nombre'], novela['autor'], novela['year'])