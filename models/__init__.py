from config.db import app, db

from.AdministradorModel import Admin
from.EmpresaModel import EMP
from.VendedoresModel import Vendedor
from.ProveedoresModel import Proveedor

with app.app_context():
    db.create_all()

