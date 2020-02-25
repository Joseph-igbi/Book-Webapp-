
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= os.getenv('DATABASE_URI')
db = SQLAlchemy(app)
app.config['SECRET_KEY']= os.getenv('SECRET_KEY')


bootstrap = Bootstrap(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes
