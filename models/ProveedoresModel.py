from config.db import app, db, ma 

class Proveedor(db.Model):
    __tablename__ = 'Proveedor'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.Integer)
    company_id = db.Column(db.Integer, db.ForeignKey('EMP.companyid'))

    empresa = db.relationship('EMP', backref=db.backref('proveedores', lazy=True))
    
    def __init__(self,id, nombre, email, direccion, telefono, company_id):
      self.id = id
      self.nombre = nombre
      self.email = email
      self.direccion = direccion
      self.telefono = telefono
      self.company_id = company_id
      
with app.app_context():
    db.create_all()

class ProveedoresSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'email', 'direccion', 'telefono')