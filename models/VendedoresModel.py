from config.db import app, db, ma 

class Vendedor(db.Model):
    __tablename__ = 'Vendedores'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    email = db.Column(db.String(50))
    fecha_inicio = db.Column(db.Date)
    user = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    
    def __init__(self, id, nombre, email, fecha_inicio, user, password):
      self.id = id
      self.nombre = nombre
      self.email = email
      self.fecha_inicio = fecha_inicio
      self.user = user
      self.password = password
    
with app.app_context():
    db.create_all()

class VendedorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'email', 'fecha_inicio', 'user','password')