# import app and run server
import os
from app import create_dev_app

app = create_dev_app(os.getenv('FLASK_CONFIG') or 'default')
