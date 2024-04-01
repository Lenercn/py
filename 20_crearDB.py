import sqlite3
conexion=sqlite3.connect('novelas.db')
consulta=conexion.cursor()
tabla="create table tabla(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,nombre varchar(30) not null,autor varchar (40) not null,year INTEGER(9) not null);"
print(tabla)

if (consulta.execute(tabla)):
    print('tabla creada')
else:
    print('F, NO SE CREO')

consulta.close()
conexion.commit()
conexion.close()


# import sqlite3

# # Conectar a la base de datos
# db1 = sqlite3.connect('novelas.db')

# # Crear un cursor
# consulta = db1.cursor()

# # Obtener información de los campos de la tabla 'tabla'
# consulta.execute("PRAGMA table_info(tabla);")

# # Recuperar y mostrar la información
# campos = consulta.fetchall()
# for campo in campos:
#     print(campo)

# # Cerrar el cursor y la conexión
# consulta.close()
# db1.close()
