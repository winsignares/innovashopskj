from config.bd import app, db, ma 

class EMP(db.Model):
    __tablename__ = 'EMP'
    
    companyid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_emp = db.Column(db.String(50), unique=True)
    mail_emp = db.Column(db.String(50))
    ubicacion = db.Column(db.String(50))
    status = db.Column(db.String(50))
    IVA = db.Column(db.String(50))
    fecha_Inicio = db.Column(db.String(50))
    fecha_final = db.Column(db.String(50))
    
    def __init__(self, name_emp, mail_emp, ubicacion, status, IVA, fecha_Inicio, fecha_final):
      self.name_emp = name_emp
      self.mail_emp = mail_emp
      self.ubicacion = ubicacion
      self.status = status
      self.IVA = IVA
      self.fecha_Inicio = fecha_Inicio
      self.fecha_final = fecha_final
    
with app.app_context():
    db.create_all()

class EMPSchema(ma.Schema):
    class Meta:
        fields = ('companyid', 'name_emp', 'mail_emp','ubicacion', 'status', 'IVA', 'fecha_Inicio')