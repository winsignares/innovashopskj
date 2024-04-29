from flask import Blueprint, render_template, request, redirect
from config.db import app, db, ma
from models.ProductosModel import Productos, ProductoSchema

ruta_productos = Blueprint("route_productos", __name__)

producto_schema= ProductoSchema()
productos_schema= ProductoSchema(many=True)

@app.route('/registr**oproducto', methods=['POST'])
def registrar_productos():

    nombre = request.form.get('nombre')
    preciouni = request.form.get('preciouni')
    alternos = request.form.get('alternos')
    precioventa = request.form.get('precioventa')
    cantidad = request.form.get('cantidad')
    cantidadmin = request.form.get('cantidadmin')
    iva = request.form.get('iva', 'False').lower() in ['true', '1', 't', 'yes']  # Convertir a booleano

    producto_existente = Productos.query.filter_by(nombre=nombre).first()

    if producto_existente:
        
        nuevo_producto = Productos(
            nombre=nombre,
            preciouni=float(preciouni),
            alternos=alternos,
            precioventa=float(precioventa),
            cantidad=cantidad,
            cantidadmin=cantidadmin,
            iva=iva
        )
        db.session.add(nuevo_producto)
    db.session.commit()

    return redirect('/Portal_Empresa')

@app.route('/actualizarproductos', methods=['POST'])
def actualizar():

    nombre = request.form.get('nombre')
    preciouni = request.form.get('preciouni')
    alternos = request.form.get('alternos')
    precioventa = request.form.get('precioventa')
    cantidad = request.form.get('cantidad')
    cantidadmin = request.form.get('cantidadmin')
    iva = request.form.get('iva', 'False').lower() in ['true', '1', 't', 'yes']  

    producto_existente = Productos.query.filter_by(nombre=nombre).all()

    if producto_existente:

        producto_existente.preciouni = float(preciouni)
        producto_existente.alternos = alternos
        producto_existente.precioventa = float(precioventa)
        producto_existente.cantidad = cantidad
        producto_existente.cantidadmin = cantidadmin
        producto_existente.iva = iva
    
    db.session.commit()

    return redirect('/Portal_Empresa')