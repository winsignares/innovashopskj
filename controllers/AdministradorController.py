from flask import Blueprint, render_template, request, redirect, session
from config.db import app, db, ma
from models.AdministradorModel import Admin, AdminSchema

ruta_administrador = Blueprint('route_administrador', __name__)

Admin_schema = AdminSchema()
Admin_schema = AdminSchema(many=True)

@app.route('/loginad', methods=['GET'])
def loginadmin():
    return render_template('./Admin/loginadmin.html')

@app.route('/ingresaradmin', methods=['POST'])
def ingresaradmin():
    userad = request.form['userad'].replace(' ', '')
    passwordad = request.form['passwordad']
    userad = db.session.query(Admin).filter(Admin.userad == userad, Admin.passwordad == passwordad).all()
     
    if userad:
        resultado = Admin_schema.dump([userad])
        session['usuarioad'] = resultado
        return render_template('./Admin/portalAdministrativo.html')
    else:
        return redirect('/loginad')