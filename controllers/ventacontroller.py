from flask import Blueprint, jsonify, render_template, request, redirect
from config.db import app, db, ma
from models.ClienteModel import Cliente
from models.VentaModel import Venta, VentaSchema

ruta_ventas = Blueprint("route_ventas", __name__)

venta_schema= VentaSchema()
ventas_schema= VentaSchema(many=True)


@app.route('/completar-venta', methods=['POST'])
def completar_venta():
    id_venta = request.form.get('id-venta')
    id_cliente = request.form.get('id-cliente')
    total_venta = request.form.get('totalCarrito')
    
    # Aquí puedes procesar la venta: guardar en la base de datos, etc.
    # Por ahora, simplemente imprimir los datos recibidos
    print("ID de la Venta:", id_venta)
    print("ID del Cliente:", id_cliente)
    print("Total de la Venta:", total_venta)
    
    # Simular respuesta exitosa
    return jsonify({'success': True})



@app.route('/obtener-ids-clientes', methods=['GET'])
def obtener_ids_clientes():
    ids_clientes = [cliente.id for cliente in Cliente.query.all()]
    return jsonify(ids_clientes)

