from flask import Flask, redirect, request, jsonify, json, session, render_template
from config.db import app, db

from controllers.UserController import ruta_user, User
from controllers.ArticulosController import ruta_articulos
from controllers.AdministradorController import ruta_administrador
from controllers.EmpresaController import ruta_empresa
from controllers.ProveedoresController import ruta_proveedores

app.register_blueprint(ruta_user, url_prefix="/controller")
app.register_blueprint(ruta_articulos, url_prefix="/controller")
app.register_blueprint(ruta_administrador, url_prefix="/controller")
app.register_blueprint(ruta_empresa, url_prefix="/controller")
app.register_blueprint(ruta_proveedores, url_prefix="/controller")

@app.route('/', methods=['GET'])
def index():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)