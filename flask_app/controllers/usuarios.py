from flask_app import app #Importamos la app

from flask import render_template, redirect, request, url_for
from flask_app.models.usuario import Usuario



NOMBRE_BD = 'ejercicio_8_septiempbre'

@app.route('/')
def inicio():
    return redirect(url_for("registro"))

@app.route('/registro', methods =["GET","POST"])
def registro():
    if request.method == "POST":

        datos = {
            "nombre": request.form["nombre"],
            "apellido": request.form["apellido"],
            "edad": request.form["edad"]
        }

        Usuario.save(datos)

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
    return redirect(url_for("lista"))

@app.route("/eliminar/<int:user_id>")
def eliminar(user_id):

    print("entrando a eliminar")
    print("id",user_id)
    datos ={
        "id":user_id
    }
    Usuario.eliminar(datos)
    return redirect(url_for("lista"))

