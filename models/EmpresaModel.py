from config.db import app, db, ma 
from sqlalchemy_utils import create_database, database_exists

class EMP(db.Model):
    __tablename__ = 'EMP'
    
    companyid = db.Column(db.Integer, primary_key=True)
    name_emp = db.Column(db.String(50), nullable=False)
    mail_emp = db.Column(db.String(50))
    ubicacion = db.Column(db.String(50))
    status = db.Column(db.String(50), nullable=False, default="activo")
    fecha_Inicio = db.Column(db.Date) 
    fecha_final = db.Column(db.Date)
    user = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    admin_id = db.Column(db.Integer, db.ForeignKey('administrador.id'))

    admin = db.relationship('Admin', backref=db.backref('empresas', lazy=True))
    vendedores = db.relationship('Vendedor', backref='empresa', lazy=True)
    
    def __init__(self,companyid, name_emp, mail_emp, ubicacion, status, fecha_Inicio, fecha_final, user, password, admin_id):
        self.companyid = companyid
        self.name_emp = name_emp
        self.mail_emp = mail_emp
        self.ubicacion = ubicacion
        self.status = status
        self.fecha_Inicio = fecha_Inicio
        self.fecha_final = fecha_final
        self.user = user
        self.password = password
        self.admin_id = admin_id
     
    """  
    def create_database(self):
        if not database_exists(f"mysql+pymysql://root:root@127.0.0.1/{self.name_emp}"):
            create_database(f"mysql+pymysql://root:root@127.0.0.1/{self.name_emp}")

    def bind_database(self):
        db.engine.execute(f"CREATE SCHEMA IF NOT EXISTS {self.name_emp};")
        db.engine.execute(f"ALTER ROLE username SET search_path TO {self.name_emp};")
    """ 
        
with app.app_context():
    db.create_all()

class EMPSchema(ma.Schema):
    class Meta:
        fields = ('companyid','name_emp', 'mail_emp', 'ubicacion', 'status', 'fecha_Inicio', 'fecha_final','user','password')