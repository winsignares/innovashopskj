from config.db import app, db, ma 

class Proveedor(db.Model):
    __tablename__ = 'Proveedor'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.Integer)
    
    def __init__(self,id, nombre, email, direccion, telefono ):
      self.id = id
      self.nombre = nombre
      self.email = email
      self.direccion = direccion
      self.telefono = telefono
    
with app.app_context():
    db.create_all()

class ProveedoresSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'email', 'direccion', 'telefono')