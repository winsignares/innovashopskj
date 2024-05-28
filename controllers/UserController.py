from flask import Flask, jsonify, request, redirect, session, make_response, Blueprint
from datetime import datetime, timedelta, timezone
import jwt
from models.UserModel import User, UsersSchema
from models.VendedoresModel import Vendedor, VendedorSchema
from models.EmpresaModel import EMP, EMPSchema
from models.ClienteModel import Cliente, ClientesSchema
from functools import wraps
from config.db import app, db

ruta_user = Blueprint("route_user", __name__)

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

SECRET_KEY = "pruebaToken"

def generar_fecha_vencimiento(dias=0, horas=0, minutos=0, segundos=0):
    fecha_actual = datetime.now(tz=timezone.utc)
    tiempo_vencimiento = timedelta(days=dias, hours=horas, minutes=minutos, seconds=segundos)
    return fecha_actual + tiempo_vencimiento

def generar_token(user_id):
    fecha_vencimiento = generar_fecha_vencimiento(segundos=200)
    payload = {
        "exp": fecha_vencimiento,
        "user_id": user_id,
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verificar_token(token):
    try:
        token_verif = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"error": False, "mensaje": "Token valido"}
    except jwt.ExpiredSignatureError:
        return {"error": True, "mensaje": "Token expirado"}
    except jwt.InvalidTokenError:
        return {"error": True, "mensaje": "Token invalido"}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return jsonify({'mensaje': 'Token es requerido!'}), 403
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'mensaje': 'Token ha expirado!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'mensaje': 'Token inválido!'}), 403
        return f(*args, **kwargs)
    return decorated

@app.route('/ingresar', methods=['POST'])
def ingresar():
    user = request.form['user'].replace(' ', '')
    password = request.form['password']
    
    user1 = db.session.query(User).filter(User.user == user, User.password == password).first()
    vendedor = db.session.query(Vendedor).filter(Vendedor.user == user, Vendedor.password == password).first()
    empresa = db.session.query(EMP).filter(EMP.user == user, EMP.password == password).first()
    cliente = db.session.query(Cliente).filter(Cliente.user == user, Cliente.password == password).first()

    if user1:
        token = generar_token(user1.id)
        session['usuario'] = user_schema.dump(user1)
        response = redirect('/Portal_Empresa')
        response.set_cookie('token', token)
        return response
    elif vendedor:
        token = generar_token(vendedor.id)
        session['usuario'] = user_schema.dump(vendedor)
        response = redirect('/Portal_Vendedor')
        response.set_cookie('token', token)
        return response
    elif empresa:
        token = generar_token(empresa.companyid)
        session['usuario'] = user_schema.dump(empresa)
        session['company_id'] = empresa.companyid
        response = redirect('/Portal_Empresa')
        response.set_cookie('token', token)
        return response
    elif cliente:
        token = generar_token(cliente.id)
        session['usuario'] = user_schema.dump(cliente)
        response = redirect('/Portal_Cliente')
        response.set_cookie('token', token)
        return response
    else:
        return redirect('/')

@app.route('/ruta_protegida')
@token_required
def ruta_protegida():
    return jsonify({'mensaje': 'Este es un contenido protegido'})
