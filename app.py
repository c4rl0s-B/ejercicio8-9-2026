from flask import Flask, render_template, request, redirect, session, url_for

from mysqlconnection import connectToMySQL
from usuarios import Usuario

app = Flask(__name__)

NOMBRE_BD = 'ejercicio_8_septiempbre'

@app.route('/')
def inicio():
    return redirect(url_for("registro"))

@app.route('/registro', methods =["GET","POST"])
def registro():
    if request.method == "POST":

        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        edad = request.form["edad"]

        query = """
            INSERT INTO usuarios (nombre, apellido, edad)
            VALUES (%(nombre)s, %(apellido)s, %(edad)s);
        """

        datos = {
            "nombre": nombre,
            "apellido": apellido,
            "edad":edad
        }
        mysql = connectToMySQL(NOMBRE_BD)

        mysql.query_db(query, datos)

        return redirect(url_for("lista"))

    return render_template("index.html")


@app.route('/lista_registrados', methods =["GET"])
def lista():

    usuarios = Usuario.get_all()
    print(usuarios)

    return render_template( "lista_registrados.html", usuarios=usuarios )


if __name__ == "__main__":
    app.run(debug=True)