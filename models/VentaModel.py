from config.db import app, db, ma 

class Venta(db.Model):
    __tablename__ = 'Venta'
    
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('Cliente.id'), nullable=False)
    total = db.Column(db.Float(), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    
    def __init__(self, id_cliente, total):
        self.id_cliente = id_cliente
        self.total = total
    
with app.app_context():
    db.create_all()

class VentaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_cliente', 'total')