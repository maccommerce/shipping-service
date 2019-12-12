__version__ = '0.1.0'

from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from .config.app_config import env_config
from .config import bootstrapDB
from .web.resources.shipping_fee import ShippingCost
from .web.router.blueprints import api_blueprint


api = Api(api_blueprint)
db = MongoEngine()


def create_dev_app(config_name: str) -> Flask:
    """
    Build Flask application and setup development configurations
    """
    bootstrapDB.run()
    app = Flask(__name__)
    app.config.from_object(env_config[config_name])
    env_config[config_name].init_app(app)

    api.init_app(app)
    db.init_app(app)
    api.add_resource(ShippingCost, '/cost')

    app.register_blueprint(api_blueprint)

    return app


def create_prod_app(config: str) -> Flask:
    """
    Build Flask application and setup production configurations 
    """
    
    pass




