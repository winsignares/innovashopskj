from flask import Blueprint, render_template, request, redirect
from config.db import app, db, ma
from models.ProductosModel import Productos, ProductoSchema

ruta_productos = Blueprint("route_productos", __name__)

producto_schema= ProductoSchema()
productos_schema= ProductoSchema(many=True)

@app.route('/Productos')
def indexarticulos():
    return render_template('articulos.html')

@app.route('/registrarproductos', methods=['POST'])
def actualizar():
    id = request.form['id']
    Nombre = request.form['Nombre']
    Precio = request.form['Precio']
    articulo = Productos.query.get(id)
    articulo.Nombre = Nombre
    articulo.Precio = Precio
    db.session.commit()
    return redirect('/larticulos')
