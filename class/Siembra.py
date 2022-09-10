class Siembra():
    codigo = 0
    codigo_vereda = 0
    codigo_arbol = 0
    codigo_contratista = 0
    fecha = " "
    total_arbol = 0
    total_hectarea = 0

    def __init__(self, codigo, codigo_vereda, codigo_arbol, codigo_contratista, 
                fecha, total_arbol, total_hectarea):
        self.codigo = codigo
        self.codigo_arbol = codigo_arbol
        self.codigo_contratista = codigo_contratista
        self.codigo_vereda = codigo_vereda
        self.fecha = fecha
        self.total_arbol = total_arbol
        self.total_hectarea = total_hectarea


