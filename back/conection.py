import sqlite3
import Siembra as Siembra

conexion=sqlite3.connect("./database/siembrasDB.sqlite")
salida = Siembra
consultasql = "select s.codigo, s.fecha, s.total_hectareas, s.total_arbole, s.codigo_vereda, s.codigo_arbol, s.codigo_contratista from siembras"

def __getSiembra__(codigo) -> Siembra:
    try:
        conexion.execute(consultasql)
    except:
        print("error")