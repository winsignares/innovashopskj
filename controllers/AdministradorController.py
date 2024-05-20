from flask import Blueprint, render_template, request, redirect, session, jsonify
from config.db import app, db, ma
from controllers.UserController import token_required
from models.AdministradorModel import Admin, AdminSchema
from models.EmpresaModel import EMP, EMPSchema
from datetime import datetime, timedelta, timezone
import jwt

ruta_administrador = Blueprint('route_administrador', __name__)

Admin_schema = AdminSchema()
Admins_schema = AdminSchema(many=True)

SECRET_KEY = "pruebaToken"

def generar_token_admin(user_id):
    fecha_vencimiento = datetime.now(tz=timezone.utc) + timedelta(seconds=30)
    payload = {
        "exp": fecha_vencimiento,
        "user_id": user_id,
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

@app.route('/ingresaradmin', methods=['POST'])
def ingresaradmin():
    userad = request.form['userad'].replace(' ', '')
    passwordad = request.form['passwordad']
    user = db.session.query(Admin).filter(Admin.userad == userad, Admin.passwordad == passwordad).first()
    
    if user:
        token = generar_token_admin(user.id)
        session['usuarioad'] = Admin_schema.dump(user)
        response = redirect('/portaladmin')
        response.set_cookie('token', token)
        return response
    else:
        return redirect('/loginad')
    

@app.route('/portaladmin', methods=['GET'])
@token_required
def portaladministrativo():
    
    empresas = EMP.query.all()
    if 'usuarioad' in session:
        return render_template('./Admin/portalAdministrativo.html',usuario = session['usuarioad'],  empresas=empresas)
    else:
        return redirect('/')
    


@app.route('/loginad', methods=['GET'])
def loginadmin():
    return render_template('./Admin/loginadmin.html')


@app.route('/Crearempresa')
def crearempresa():
    return render_template('./Admin/Crearempresas.html')