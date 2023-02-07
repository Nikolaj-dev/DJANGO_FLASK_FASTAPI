from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://flask:flask@localhost" \
                                        ":5432/library"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)


from models import Book
from routes import *
