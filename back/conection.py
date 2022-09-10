import sqlite3

conexion=sqlite3.connect("./database/siembrasDB.sqlite")
try:
    conexion.execute("""""")
    print("se creo la tabla articulos")                        
except sqlite3.OperationalError:
    print("error")                     
conexion.close()