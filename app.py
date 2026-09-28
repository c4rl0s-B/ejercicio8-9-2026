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

@app.route('/usuario/<int:user_id>')
def usuario(user_id):
    datos = {
        "id": user_id
    }
    usuario = Usuario.get_by_id(datos)
    return render_template('usuario.html', usuario=usuario)

@app.route('/actualizar/<int:user_id>')
def editar_html(user_id):
    datos ={
        'id': user_id
    }
    usuario = Usuario.get_by_id(datos)
    return render_template('actualizar_usuario.html', usuario=usuario)

@app.route('/Actualizar/<int:user_id>', methods=['POST'])
def actualizar(user_id):
    data = {
        "id": user_id,
        "nombre": request.form["nombre"],
        "apellido":request.form["apellido"],
        "edad":request.form["edad"]
    }
    Usuario.actualizar(data)
    return redirect(f"/usuario/{user_id}")

@app.route("/eliminar/<int:user_id>")
def eliminar(user_id):

    print("entrando a eliminar")
    print("id",user_id)
    datos ={
        "id":user_id
    }
    Usuario.eliminar(datos)
    return redirect(url_for("lista"))

if __name__ == "__main__":
    app.run(debug=True)