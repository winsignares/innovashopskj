import os
from flask import Blueprint, jsonify, render_template, request, redirect
from config.db import app, db, ma
from models.ProductosModel import Productos, ProductoSchema

ruta_productos = Blueprint("route_productos", __name__)

producto_schema= ProductoSchema()
productos_schema= ProductoSchema(many=True)

def to_float(value, default=0.0):
    try:
        return float(value) if value else default
    except ValueError:
        return default

@app.route('/registroproducto', methods=['POST'])
def registrar_productos():

    id_productos = request.form['id']
    nombre = request.form.get('nombre', '')
    preciouni = to_float(request.form.get('preciouni'), 0.0)
    alternos = request.form.get('alternos', '')
    precioventa = to_float(request.form.get('precioventa'), 0.0)
    cantidad = to_float(request.form.get('cantidad'), 0)
    cantidadmin = to_float(request.form.get('cantidadmin'), 0)
    iva = request.form.get('iva')
    img = request.files.get('img')
    
    if not nombre:
        return jsonify({"error": "El nombre es obligatorio"}), 400
    
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

@app.route('/buscar_productos', methods=['GET'])
def buscar_productos():
    termino = request.args.get('termino', '')
    productos = Productos.query.filter(Productos.nombre.ilike(f"%{termino}%")).limit(10).all()
    return jsonify([producto.nombre for producto in productos])

def safe_float(value, default=0.0):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

@app.route('/parametrizar', methods=['POST'])
def parametrizar_producto():
    id_producto = request.form.get("id_producto")
    preciouni = safe_float(request.form.get("preciouni", 0))
    precio_ganancia = safe_float(request.form.get("precio_ganancia", 0))
    iva = safe_float(request.form.get("iva", 0))
    precio_venta = safe_float(request.form.get("precio_venta", 0))

    if not id_producto:
        return jsonify({"error": "ID del producto es obligatorio"}), 400
    
    producto = Productos.query.filter_by(id=id_producto).first()

    if producto:
        producto.preciouni = preciouni
        producto.precio_venta = precio_venta
        producto.precio_ganancia = precio_ganancia
        producto.iva = iva
        
        db.session.commit()

        return redirect("/Portal_Vendedor")
    else:
        return jsonify({"error": "Producto no encontrado"}), 404


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