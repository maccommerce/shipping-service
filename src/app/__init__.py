__version__ = '0.1.0'

from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from .config.app_config import ServiceConfig, DevConfig
from .config import bootstrapDB
from .web.resources.shipping_fee import ShippinCost


bootstrapDB.run()

app = Flask(__name__)
app.config.from_object(DevConfig)
api = Api(app)
db = MongoEngine(app)
jwt = JWTManager(app)

api.add_resource(ShippinCost, '/cost')



# from app import resources, web