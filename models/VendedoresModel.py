from config.db import app, db, ma 

class Vendedor(db.Model):
    __tablename__ = 'Vendedores'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50))
    fecha_inicio = db.Column(db.Date)
    
    def __init__(self, id, nombre, email, fecha_inicio):
      self.id = id
      self.nombre = nombre
      self.email = email
      self.fecha_inicio = fecha_inicio
    
    def __repr__(self):
        return f'<Nombre {self.nombre}>'
    
with app.app_context():
    db.create_all()

class VendedorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'email', 'fecha_inicio')