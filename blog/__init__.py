import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import datetime

app = Flask(__name__)


############################
# DATABASE SETUP ########
#####################################
# basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/flask-blog'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#################################################

# LOGIN CONFIGS

#########################
login_manager = LoginManager()

login_manager.init.app(app)
login_manager.login_view = 'users.login'

#########################################

from blog.core.views import core
app.register_blueprint(core)