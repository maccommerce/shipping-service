__version__ = '0.1.0'

from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from .config.app_config import ServiceConfig


app = Flask(__name__)
app.config.from_object(ServiceConfig)
api = Api(app)
db = MongoEngine(app)


from app import resources, web