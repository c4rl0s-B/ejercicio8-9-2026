from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    flash
)

from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.secret_key = "fjwefwein"
bcrypt = Bcrypt(app)

NOMBRE_BD = ''

@app.route('/', methods =["GET"])
def inicio():
    if request.methods == "POST"

        Usuario = request.form["usuario"]

        password = request.form["password"]

        usuario = Usuario.get_by_email("correo")
        
        password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

        query = f"INSERT INTO usuarios (usuarios, password) VALUES('{usuario}','{password}')"

        mysql = connectToMySQL(NOMBRE_BD)

        mysql.query_db(query)

        return redirect(url_for("login"))

    return render_template("index.html")

@app.route('/lista_registrados', methods =["GET"])
def lista():

