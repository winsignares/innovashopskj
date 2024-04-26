from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123Sebas@127.0.0.1/innovashop'   #(Base de datos Sebastian)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/web'    #(Base de datos Keiler)
#pp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234567890@localhost/web'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "claveSecreta"

db = SQLAlchemy(app)

ma = Marshmallow(app)
