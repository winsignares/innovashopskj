import os
from flask import Blueprint, jsonify, render_template, request, redirect
from config.db import app, db, ma
from models.ProductosModel import Productos, ProductoSchema

ruta_productos = Blueprint("route_productos", __name__)

producto_schema= ProductoSchema()
productos_schema= ProductoSchema(many=True)

@app.route('/registroproducto', methods=['POST'])
def registrar_productos():

    id_productos = request.form['id']
    nombre = request.form['nombre']
    preciouni = request.form['preciouni']
    alternos = request.form['alternos']
    precioventa = request.form['precioventa']
    cantidad = request.form['cantidad']
    cantidadmin = request.form['cantidadmin']
    iva = request.form.get('iva', 'False').lower() in ['true', '1', 't', 'yes']
    img = request.files['img']
    if img:
        filename = f"{nombre}.jpg"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        img.save(file_path)

    producto_existente = Productos.query.filter_by(id=id_productos).all()

    if producto_existente:
        return jsonify({"error": "Este producto ya existe."}), 409
    
    nuevo_producto = Productos(
            id=id_productos,
            nombre=nombre,
            preciouni=float(preciouni),
            alternos=alternos,
            precioventa=float(precioventa),
            cantidad=cantidad,
            cantidadmin=cantidadmin,
            iva=iva,
            img=filename
        )
    db.session.add(nuevo_producto)   
    db.session.commit()

    return redirect('/Portal_Vendedor')

@app.route('/actualizarproducto', methods=['POST'])
def actualizar():

    id_productos = request.form.get('id')
    nombre = request.form.get('nombre')
    preciouni = request.form.get('preciouni')
    alternos = request.form.get('alternos')
    precioventa = request.form.get('precioventa')
    cantidad = request.form.get('cantidad')
    cantidadmin = request.form.get('cantidadmin')
    iva = request.form.get('iva', 'False').lower() in ['true', '1', 't', 'yes'] 
    img = request.files.get('img') 

    producto_existente = Productos.query.filter_by(id=id_productos).first()

    if producto_existente:

        if img:
            
            filename = f"{nombre}.jpg"  
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            img.save(file_path)
            producto_existente.img = filename

        producto_existente.nombre = nombre
        producto_existente.preciouni = float(preciouni)
        producto_existente.alternos = alternos
        producto_existente.precioventa = float(precioventa)
        producto_existente.cantidad = cantidad
        producto_existente.cantidadmin = cantidadmin
        producto_existente.iva = iva
        
        db.session.commit()
        
    else:
        return jsonify({"error": "Este producto no existe."}), 409

    return redirect('/Portal_Vendedor')