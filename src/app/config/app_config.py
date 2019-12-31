import os
from dotenv import load_dotenv


load_dotenv()


class Config(object):
    HOST = '0.0.0.0'
    JWT_SECRET_KEY = os.environ['SECRET_KEY'] or 'very-shady-secret'
    MONGODB_SETTINGS = {
        'db': 'shipping',
        'host': os.environ["DATABASE_URL"]+'shipping',
        'username': os.environ['MONGO_INITDB_ROOT_USERNAME'],
        'password': os.environ['MONGO_INITDB_ROOT_PASSWORD']
    }

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING=True


class DevelopmentConfig(Config):
    DEBUG=True

env_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'test': TestingConfig,

    'default': DevelopmentConfig,
}