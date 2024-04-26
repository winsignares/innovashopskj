from flask import Blueprint, render_template, request, redirect
from config.db import app, db, ma
from models.ProductosModel import Articulos, ArticuloSchema

ruta_articulos = Blueprint("route_articulos", __name__)

articulo_schema= ArticuloSchema()
articulos_schema= ArticuloSchema(many=True)

@app.route('/Articulos')
def indexarticulos():
    return render_template('articulos.html')

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
