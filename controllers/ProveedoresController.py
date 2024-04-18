from flask import Blueprint, render_template, request, redirect
from config.db import app, db, ma
from models.ProveedoresModel import Proveedor, ProveedoresSchema

ruta_proveedores = Blueprint("route_proveedores", __name__)

proveedor_schema= ProveedoresSchema()
proveedores_schema= ProveedoresSchema(many=True)

@app.route('/proveedores', methods=['GET'])
def proveedores():
    return render_template('proveedores.html')