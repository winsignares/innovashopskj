from flask import Blueprint, Flask, render_template,json, jsonify, redirect, session, request
from config.db import app, db, ma
from models.UserModel import User, UsersSchema

ruta_user = Blueprint("route_user", __name__)

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

@app.route('/ingresar', methods=['POST'])
def ingresar():
    user = request.form['user'].replace(' ', '')
    password = request.form['password']
    user = db.session.query(User).filter(User.user == user, User.password == password).first()
     
    if user:
        resultado = user_schema.dump(user)
        session['usuario'] = resultado
        
        if resultado['rol'] == 'empresa':
            return redirect('/Portal_Empresa')
        elif resultado['rol'] == 'cliente':
            return redirect('/Portal_Cliente')
        elif resultado['rol'] == 'vendedor':
            return redirect('/Portal_Vendedor')
    else:
        return redirect('/')
    
@app.route('/Portal_Empresa', methods=['GET'])
def portalempresa():
    
    if 'usuario' in session:
        return render_template("./Portales/Portal_Empresa.html", usuario = session['usuario'])
    else:
        return redirect('/')
    
@app.route('/Portal_Cliente', methods=['GET'])
def portalcliente():
    
    if 'usuario' in session:
        return render_template("./Portales/Portal_Cliente.html", usuario = session['usuario'])
    else:
        return redirect('/')
    
@app.route('/Portal_Vendedor')
def portalvendedor():
    if 'usuario' in session:
        return render_template("./Portales/Portal_Vendedores.html")
    else:
        return redirect('/')
    
@app.route('/cerrar')
def cerrar():
    session.pop('usuario',None)
    return redirect('/')
