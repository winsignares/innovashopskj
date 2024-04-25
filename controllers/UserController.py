from flask import Blueprint, Flask, render_template,json, jsonify, redirect, session, request
from config.db import app, db, ma
from models.UserModel import User, UsersSchema
from models.VendedoresModel import Vendedor, VendedorSchema


ruta_user = Blueprint("route_user", __name__)

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

@app.route('/ingresar', methods=['POST'])
def ingresar():
    user = request.form['user'].replace(' ', '')
    password = request.form['password']
    user1 = db.session.query(User).filter(User.user == user, User.password == password).first()
    user2 = db.session.query(Vendedor).filter(Vendedor.user == user, Vendedor.password == password).first()
     
    if user1:
        resultado1 = user_schema.dump(user1)
        session['usuario'] = resultado1
    
        return redirect('/Portal_Empresa')
    elif user2:
        resultado2 = user_schema.dump(user2)
        session['usuario'] = resultado2
    
        return redirect('/Portal_Vendedor')
    else:
        return redirect('/')
    
@app.route('/Portal_Cliente', methods=['GET'])
def portalcliente():
    
    if 'usuario' in session:
        return render_template("./Portales/Portal_Cliente.html", usuario = session['usuario'])
    else:
        return redirect('/')
    
