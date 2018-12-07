from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']='7675d4fad1d19e9a8454a4c6e3ec77fa'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///biz.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
from main import routes