import os
from flask import Flask
from database.db import db
from flask_smorest import Api

import database.models


from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

import pymysql
pymysql.install_as_MySQLdb()

load_dotenv()


def create_app(db_url = None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    

    api = Api(app)

    with app.app_context():
        db.create_all()
    
    return app




