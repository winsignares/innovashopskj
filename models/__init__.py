from config.db import app, db

from.AdministradorModel import Admin
from.EmpresaModel import EMP
from.VendedoresModel import Vendedor
from.ProveedoresModel import Proveedor
from.ClienteModel import Cliente
from.ProductosModel import Productos


with app.app_context():
    db.create_all()

