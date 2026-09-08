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