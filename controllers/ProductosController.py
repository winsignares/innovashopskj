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
    cantidad = int(to_float(request.form.get('cantidad'), 0))
    cantidadmin = int(to_float(request.form.get('cantidadmin'), 0))
    iva = to_float(request.form.get('iva'), 0.0)
    img = request.files.get('img')
    
    if not nombre:
        return jsonify({"error": "El nombre es obligatorio"}), 400
    
    filename = None
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
            preciouni=preciouni,
            alternos=alternos,
            precioventa=precioventa,
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
    
    if not termino:
        return jsonify([])
    
    productos = Productos.query.filter(Productos.nombre.ilike(f"%{termino}%")).limit(10).all()
    
    return jsonify([{'id': producto.id, 'nombre': producto.nombre} for producto in productos])

@app.route('/parametrizar', methods=['POST'])
def parametrizar_producto():
    id_producto = request.form.get("id")
    preciouni = to_float(request.form.get("preciouni", 0))
    precio_ganancia = to_float(request.form.get("precio_ganancia", 0))
    iva = to_float(request.form.get("iva", 0))
    
    if not id_producto:
        return jsonify({"error": "ID del producto es obligatorio"}), 400
    
    producto = Productos.query.filter_by(id=id_producto).first()

    if producto:
        ganancia = preciouni * (precio_ganancia / 100)
        precio_venta = preciouni + ganancia
        precio_venta += precio_venta * (iva / 100)  
        
        producto.preciouni = preciouni
        producto.precio_ganancia = precio_ganancia
        producto.iva = iva
        producto.precioventa = precio_venta
        
        db.session.commit()

        return redirect("/Portal_Vendedor")
    else:
        return jsonify({"error": "Producto no encontrado"}), 404

@app.route('/actualizarproducto', methods=['POST'])
def actualizar():
    id_productos = request.form.get('id')
    nombre = request.form.get('nombre')
    alternos = request.form.get('alternos')
    cantidad = int(request.form.get('cantidad'))
    cantidadmin = int(request.form.get('cantidadmin'))
    img = request.files.get('img') 

    producto_existente = Productos.query.filter_by(id=id_productos).first()

    if producto_existente:
        if img:
            filename = f"{nombre}.jpg"  
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            img.save(file_path)
            producto_existente.img = filename

        producto_existente.nombre = nombre
        producto_existente.alternos = alternos
        producto_existente.cantidad = cantidad
        producto_existente.cantidadmin = cantidadmin
        
        db.session.commit()
    else:
        return jsonify({"error": "Este producto no existe."}), 409

    return redirect('/Portal_Vendedor')

@app.route('/vender_producto', methods=['POST'])
def vender_producto():
    producto_id = request.form['producto_id']
    cantidad = int(request.form['cantidad'])

    producto = Productos.query.get(producto_id)
    if producto:
        if producto.cantidad >= cantidad:
            producto.cantidad -= cantidad
            db.session.commit()
            return jsonify({"message": "Venta realizada con éxito", "stock_actual": producto.cantidad})
        else:
            return jsonify({"error": "Stock insuficiente"}), 400
    else:
        return jsonify({"error": "Producto no encontrado"}), 404

@app.route('/ingresar_producto', methods=['POST'])
def ingresar_producto():
    producto_id = request.form['producto_id']
    cantidad = int(request.form['cantidad'])

    producto = Productos.query.get(producto_id)
    if producto:
        producto.cantidad += cantidad
        db.session.commit()
        return jsonify({"message": "Stock actualizado con éxito", "stock_actual": producto.cantidad})
    else:
        return jsonify({"error": "Producto no encontrado"}), 404

@app.route('/obtener_productos', methods=['GET'])
def obtener_productos():
    productos = Productos.query.all()
    productos_info = []

    for producto in productos:
        productos_info.append({
            "id": producto.id,
            "nombre": producto.nombre,
            "cantidad": producto.cantidad,
            "color": producto.actualizar_color()
        })
    
    return jsonify(productos_info)
