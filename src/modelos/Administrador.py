from config.bd import app, db, ma 

class Admin(db.Model):
    __tablename__ = 'administrador'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userad = db.Column(db.String(50), unique=True)
    passwordad = db.Column(db.String(50))
    
    def __init__(self, userad, passwordad):
      self.userad = userad
      self.passwordad = passwordad
    
with app.app_context():
    db.create_all()

class AdminSchema(ma.Schema):
    class Meta:
        fields = ('id', 'userad', 'passwordad')