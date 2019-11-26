import os
from dotenv import load_dotenv


load_dotenv()


class ServiceConfig(object):
    JWT_SECRET_KEY = 'your-256-bit-secret'
    MONGODB_SETTINGS = {
        'db': 'shipping',
        'host': os.environ["DATABASE_URL"]+'shipping',
        'username': os.environ['MONGO_INITDB_ROOT_USERNAME'],
        'password': os.environ['MONGO_INITDB_ROOT_PASSWORD']
    }


class DevConfig(object):

    JWT_SECRET_KEY = 'your-256-bit-secret'
    MONGODB_SETTINGS = {
        'db': 'shipping',
        'host': os.environ["DATABASE_URL"]+'shipping',
        'username': os.environ['MONGO_INITDB_ROOT_USERNAME'],
        'password': os.environ['MONGO_INITDB_ROOT_PASSWORD']
    }
