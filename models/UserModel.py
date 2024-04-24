from config.db import app, db, ma 

class User(db.Model):
    __tablename__ = 'User'
    
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    rol = db.Column(db.String(30))
    
    def __init__(self, user, password, rol):
      self.user = user
      self.password = password
      self.rol = rol
    
    def __repr__(self):
        return f'<User {self.user}>'
    
with app.app_context():
    db.create_all()

class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user', 'password', 'rol')