from .config import Config
from flask import Flask

from flask_cors import CORS

# from app import cli
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__, static_folder="./dist/static", template_folder="./dist")


app.config.from_object(Config)

CORS(app, resources={r'/*': {'origins': '*'}})

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models
