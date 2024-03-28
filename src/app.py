from flask import Flask, redirect, request, jsonify, json, session, render_template

from config.bd import app, db
from modelos.Articulos import Articulos, ArticuloSchema
from modelos.User import User, UsersSchema

articulo_schema= ArticuloSchema()
articulos_schema= ArticuloSchema(many=True)

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

@app.route('/', methods=['GET'])
def index():
    
    return render_template("login.html")

@app.route('/ingresar', methods=['POST'])
def ingresar():
    user = request.form['user']
    password = request.form['password']
    user = db.session.query(User).filter(User.user == user, User.password == password).all()
    
    
    if user:
        resultado = users_schema.dump([user])
        session['usuario'] = resultado
        return redirect('/larticulos')
    else:
        return redirect('/')
    
@app.route('/larticulos', methods=['GET'])
def larticulos():
    
    if 'usuario' in session:
        return render_template("larticulos.html", usuario = session['usuario'])
    else:
        return redirect('/')
    
@app.route('/cerrar')
def cerrar():
    session.pop('usuario',None)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)