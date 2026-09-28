from mysqlconnection import connectToMySQL
NOMBRE_BD = 'ejercicio_8_septiempbre'

class Usuario:

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.edad = data["edad"]


    @classmethod
    def get_all(cls):

        query = """
            SELECT *
            FROM usuarios;
        """

        resultados = connectToMySQL(NOMBRE_BD).query_db(query)

        usuarios = []

        for usuario in resultados:
            usuarios.append(cls(usuario))

        return usuarios

    @classmethod
    def get_by_id(cls,data):
        query = """
        select *
        FROM usuarios
        WHERE id = %(id)s;
        """

        resultado = connectToMySQL(NOMBRE_BD).query_db(query, data)
        if len(resultado) < 1:
            return None
        
        return cls(resultado[0])

    @classmethod
    def actualizar(cls,data):
        query = """
            UPDATE usuarios
            SET nombre = %(nombre)s,
                apellido = %(apellido)s,
                eded = %(edad)s
            WHERE id = %(id)s;
            """
        return connectToMySQL(NOMBRE_BD).query_db(query, data)

    @classmethod
    def eliminar(cls, data):
        query = """
            DELETE FROM usuarios
            WHERE id = %(id)s;
        """
        return connectToMySQL(NOMBRE_BD).query_db(query,data)