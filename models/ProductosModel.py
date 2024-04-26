from config.db import db, ma, app

class Productos (db.Model):
    __tablename__ = "Producto"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(70), unique=True)
    preciouni = db.Column(db.Float())
    alternos = db.Column(db.String(70))
    precioventa = db.Column(db.Float())
    cantidad = db.Column(db.String(70))
    cantidadmin = db.Column(db.String(70))
    iva = db.Column(db.Boolean, default=False)
    
    def __init__(self, nombre, preciouni, alternos, precioventa, cantidad, cantidadmin, iva=False):
        self.nombre = nombre  
        self.preciouni = preciouni  
        self.alternos = alternos  
        self.precioventa = precioventa  
        self.cantidad = cantidad 
        self.cantidadmin = cantidadmin  
        self.iva = iva
    
with app.app_context():
    db.create_all()

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'preciouni', 'alternos', 'precioventa', 'cantidad', 'cantidadmin', 'iva')