from config.db import db, ma, app

class Productos(db.Model):
    __tablename__ = "Producto"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(70), unique=True)
    preciouni = db.Column(db.Float())
    alternos = db.Column(db.String(70))
    precioventa = db.Column(db.Float())
    cantidad = db.Column(db.Integer)  # Cambiar a Integer para manejar la cantidad como número
    cantidadmin = db.Column(db.Integer)  # Cambiar a Integer para manejar la cantidad mínima como número
    iva = db.Column(db.Float())
    img = db.Column(db.String(255), nullable=True)
    # proveedor_id = db.Column(db.Integer, db.ForeignKey('Proveedor.id'))
    # empresa_id = db.Column(db.Integer, db.ForeignKey('EMP.companyid'))

    # proveedor = db.relationship('Proveedor', backref=db.backref('productos', lazy=True))
    # empresa = db.relationship('EMP', backref=db.backref('productos', lazy=True))

    def __init__(self, id, nombre, preciouni, alternos, precioventa, cantidad, cantidadmin, iva, img=None):
        self.id = id
        self.nombre = nombre  
        self.preciouni = preciouni  
        self.alternos = alternos  
        self.precioventa = precioventa  
        self.cantidad = cantidad 
        self.cantidadmin = cantidadmin  
        self.iva = iva
        self.img = img

    def actualizar_color(self):
        if self.cantidad < self.cantidadmin:
            return 'rojo'
        elif self.cantidad <= self.cantidadmin * 1.5:
            return 'amarillo'
        else:
            return 'verde'

with app.app_context():
    db.create_all()

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'preciouni', 'alternos', 'precioventa', 'cantidad', 'cantidadmin', 'iva', 'img', 'color')
