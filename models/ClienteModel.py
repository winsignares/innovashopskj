from config.db import app, db, ma 

class Cliente(db.Model):
    __tablename__ = 'Cliente'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.Integer)
    user = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    
    def __init__(self, id,nombre, email, direccion, telefono, user, password):
      self.id = id
      self.nombre = nombre
      self.email = email
      self.direccion = direccion
      self.telefono = telefono
      self.user = user
      self.password = password
    
with app.app_context():
    db.create_all()

class ClientesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'email', 'direccion', 'telefono', 'user','password')