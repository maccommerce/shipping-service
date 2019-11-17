__version__ = '0.1.0'

from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from .config.app_config import ServiceConfig
from .web.resources.shipping_fee import ShippinCost

app = Flask(__name__)
app.config.from_object(ServiceConfig)
api = Api(app)
db = MongoEngine(app)

api.add_resource(ShippinCost, '/cost')

from app import resources, web