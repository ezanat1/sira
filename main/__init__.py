from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail



app = Flask(__name__)
app.config['SECRET_KEY']='7675d4fad1d19e9a8454a4c6e3ec77fa'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///biz.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

app.config['MAIL_SERVER']='smpt.googlemail.com'
app.config['MAIL_PORT']='587'
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']='ezex.55@gmail.com'
app.config['MAIL_PASSWORD']='Sabi@ezex123'

mail=Mail(app)
from main import routes