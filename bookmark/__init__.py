import os
from flask import Flask
from flask_jwt import JWT
from flask_cors import CORS
from dotenv import load_dotenv
from flask_compress import Compress
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

# Load from cfg file its stranger
# app = Flask(__name__, instance_relative_config=True)
# app.config.from_pyfile('config.cfg', silent=True) 

# Extensions
app = Flask(__name__)
CORS(app)
Compress(app)

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)

from .auth import authenticate, identity
JWT(app, authenticate, identity)

# Blueprints
from bookmark.views import books_resource, users_resource
app.register_blueprint(books_resource, url_prefix='/books')
app.register_blueprint(users_resource, url_prefix='/auth')

db.create_all()