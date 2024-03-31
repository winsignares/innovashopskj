from flask import Flask, redirect, request, jsonify, json, session, render_template
from config.bd import app, db
from modelos.Articulos import Articulos, ArticuloSchema
from modelos.User import User, UsersSchema
from modelos.Administrador import Admin, AdminSchema
from modelos.EMP import EMP, EMPSchema

articulo_schema= ArticuloSchema()
articulos_schema= ArticuloSchema(many=True)

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

Admin_schema = AdminSchema()
Admin_schema = AdminSchema(many=True)

EMP_schema = EMPSchema()
EMP_schema = EMPSchema(many=True)

@app.route('/', methods=['GET'])
def index():
    
    return render_template("login.html")

@app.route('/ingresar', methods=['POST'])
def ingresar():
    user = request.form['user'].replace(' ', '')
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
    session.clear()
    return redirect('/')

@app.route('/actualizar', methods=['POST'])
def actualizar():
    id = request.form['id']
    Nombre = request.form['Nombre']
    Precio = request.form['Precio']
    articulo = Articulos.query.get(id)
    articulo.Nombre = Nombre
    articulo.Precio = Precio
    db.session.commit()
    return redirect('/larticulos')

@app.route('/loginad', methods=['GET'])
def loginadmin():
    
    return render_template('loginadmin.html')

@app.route('/ingresaradmin', methods=['POST'])
def ingresarModoAdmin():
    userad = request.form['userad'].replace(' ', '')
    passwordad = request.form['passwordad']
    userad = db.session.query(Admin).filter(Admin.userad == userad, Admin.passwordad == passwordad).all()

    if userad:
        resultado = Admin_schema.dump([userad])
        session['usuarioad'] = resultado
        return redirect('/Pagadmin.html')
    else:
        return redirect('/loginad')
    
@app.route('/Pagadmin.html', methods=['GET'])
def paginadmin():
    
    if 'usuarioad' in session:
        return render_template("Pagadmin.html", usuarioad = session['usuarioad'])
    else:
        return redirect('/loginad')

# Ruta para editar una empresa
@app.route('/empresas/editar/<id>', methods=['GET'])
def editar_empresa(id):
  empresa = EMP.query.get(id)
  if empresa:
    # Devuelve solo el objeto empresa en formato JSON
    return jsonify(EMP_schema.dump(empresa))
  else:
    return jsonify({"error": "Empresa no encontrada"})


# Ruta para eliminar una empresa
@app.route('/empresas/eliminar/<id>', methods=['DELETE'])
def eliminar_empresa(id):
    empresa = EMP.query.get(id)
    if empresa:
        db.session.delete(empresa)
        db.session.commit()
        return jsonify({"success": "Empresa eliminada"})
    else:
        return jsonify({"error": "Empresa no encontrada"})

# Ruta para crear una empresa
@app.route('/empresas/crear', methods=['POST'])
def crear_empresa():

    nombre_emp = request.form['nombre_emp']
    id = request.form['companyid']
    mail_emp = request.form['mail_emp']
    ubicacion = request.form['ubicacion']
    status = request.form['status']
    IVA = request.form['IVA']
    fecha_Inicio = request.form['fecha_Inicio']
    fecha_final = request.form['fecha_final']

    empresa = EMP.query.get(id)

    if not empresa:
        empresa = EMP(
        nombre_emp=nombre_emp,
        mail_emp=mail_emp,
        ubicacion=ubicacion,
        status=status,
        IVA=IVA,
        fecha_Inicio=fecha_Inicio,
        fecha_final=fecha_final
    )

    empresa.nombre_emp = nombre_emp
    empresa.mail_emp = mail_emp
    empresa.ubicacion = ubicacion
    empresa.status = status
    empresa.IVA = IVA
    empresa.fecha_Inicio = fecha_Inicio
    empresa.fecha_final = fecha_final

    try:

        db.session.add(empresa)  
        db.session.commit()

        return redirect('/Pagadmin.html')
    except Exception as e:

        return jsonify({"error": str(e)})


@app.route('/Crearempresas.html', methods=['GET'])
def crearemp():
  
  return render_template('/Crearempresas.html')


if __name__ == "__main__":
    app.run(debug=True)