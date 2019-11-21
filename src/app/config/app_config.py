

class ServiceConfig(object):
    JWT_SECRET_KEY = 'your-256-bit-secret'
    MONGODB_SETTINGS = {
        'db': 'shipping',
        'host': 'mongodb://localhost/shipping'
    }