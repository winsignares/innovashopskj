from config.db import app, db, ma 

class EMP(db.Model):
    __tablename__ = 'EMP'
    
    companyid = db.Column(db.Integer, primary_key=True)
    name_emp = db.Column(db.String(50), nullable=False)
    mail_emp = db.Column(db.String(50))
    ubicacion = db.Column(db.String(50))
    status = db.Column(db.String(50))
    fecha_Inicio = db.Column(db.Date) 
    fecha_final = db.Column(db.Date)
    user = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    
    def __init__(self,companyid, name_emp, mail_emp, ubicacion, status, fecha_Inicio, fecha_final, user, password):
        self.companyid = companyid
        self.name_emp = name_emp
        self.mail_emp = mail_emp
        self.ubicacion = ubicacion
        self.status = status
        self.fecha_Inicio = fecha_Inicio
        self.fecha_final = fecha_final
        self.user = user
        self.password = password
    
with app.app_context():
    db.create_all()

class EMPSchema(ma.Schema):
    class Meta:
        fields = ('companyid','name_emp', 'mail_emp', 'ubicacion', 'status', 'fecha_Inicio', 'fecha_final','user','password')