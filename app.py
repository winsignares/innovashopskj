from flask import Flask, make_response, redirect, request, jsonify, json, session, render_template
from config.db import app, db

from controllers.UserController import ruta_user, User
from controllers.ProductosController import ruta_productos
from controllers.AdministradorController import ruta_administrador
from controllers.EmpresaController import ruta_empresa
from controllers.ProveedoresController import ruta_proveedores
from controllers.VendedorController import ruta_vendedor
from controllers.ClienteController import ruta_clientes

app.register_blueprint(ruta_user, url_prefix="/controller")
app.register_blueprint(ruta_productos, url_prefix="/controller")
app.register_blueprint(ruta_administrador, url_prefix="/controller")
app.register_blueprint(ruta_empresa, url_prefix="/controller")
app.register_blueprint(ruta_proveedores, url_prefix="/controller")
app.register_blueprint(ruta_vendedor, url_prefix="/controller")
app.register_blueprint(ruta_clientes, url_prefix="/controller")
app.config['UPLOAD_FOLDER'] = 'config/static/img/Img-productos/' 
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 


@app.route('/', methods=['GET'])
def index():
    return render_template("login.html")

@app.route("/")
def login():
    response = make_response(render_template("login.html"))
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, post-check=0, pre-check=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

if __name__ == "__main__":
    app.run(debug=True)