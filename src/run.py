# import app and run server
import os
from app import create_prod_app, db

app = create_prod_app(os.getenv('FLASK_CONFIG') or 'default')
