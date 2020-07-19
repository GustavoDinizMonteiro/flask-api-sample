import os
from flask import Flask
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

# Blueprints
from bookmark.views import jwt, books_resource, auth_resource
jwt.init_app(app)
app.register_blueprint(auth_resource, url_prefix='/auth')
app.register_blueprint(books_resource, url_prefix='/books')

db.create_all()