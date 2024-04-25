from flask import Blueprint, Flask, render_template,json, jsonify, redirect, session, request
from config.db import app, db, ma
from models.VendedoresModel import Vendedor, VendedorSchema

ruta_vendedor = Blueprint("route_vendedor", __name__)

user_schema = VendedorSchema()
users_schema = VendedorSchema(many=True)

@app.route('/registrovendedor', methods=['POST'])
def registrar_vendedor():
    if request.method == 'POST':
        id_vendedor = request.form['id']
        Nombre = request.form['nombre']
        Email = request.form['email'] 
        Fecha_inicio = request.form['fecha_inicio']

        vendedor_existente = Vendedor.query.filter_by(id=id_vendedor).all()
        
        if vendedor_existente:
            return jsonify({"error": "El ID ya esta en uso."}), 409
        
        nuevo_vendedor = Vendedor(
            id=id_vendedor,
            nombre=Nombre,
            email=Email,
            fecha_inicio=Fecha_inicio
        )

        db.session.add(nuevo_vendedor)
        db.session.commit()

    return redirect('/Portal_Empresa/')


@app.route('/Portal_Empresa/', methods=['GET'])
def ver_vendedores():
    vendedores = Vendedor.query.all()
    return render_template('./Portales/Portal_Empresa.html', vendedores=vendedores)
    