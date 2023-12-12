from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from flask_restful import Api


db = SQLAlchemy()
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

objbank = Blueprint('objbank', __name__, url_prefix='/objbank')
api = Api(objbank)

app.config['SWAGGER'] = {'title': os.environ.get("APP_NAME")}


if not (os.environ.get("SQLALCHEMY_DATABASE_URI") == None):
    DB_URI = f'postgresql://{os.environ.get("DATABASE_USER")}:{os.environ.get("DATABASE_PW")}@{os.environ.get("DATABASE_HOST")}:{os.environ.get("DATABASE_PORT")}/{os.environ.get("DATABASE_NAME")}'
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

app.config["JSON_SORT_KEYS"] = False

cors = CORS(app, resources={r"/*": {"origins": "*"}})

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']
