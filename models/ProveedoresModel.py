from config.db import app, db, ma 

class Proveedor(db.Model):
    __tablename__ = 'Proveedor'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50), unique=True)
    mail = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    
    def __init__(self, name, mail, address, phone ):
      self.name = name
      self.mail = mail
      self.address = address
      self.phone = phone
    
with app.app_context():
    db.create_all()

class ProveedoresSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'mail', 'address', 'phone')