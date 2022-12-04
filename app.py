"""
Main module
"""

import logging
import os

from flask import Flask
from flask_cors import CORS

import config
from api import api
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config.update(
    CORS_HEADERS='Content-Type'
)
logger = logging.getLogger()

def create_app():
   logger.info(f'Starting app in {config.APP_ENV} environment')
   app = Flask(__name__)
   app.config.from_object('config')
   api.init_app(app)
   # initialize SQLAlchemy
   #db.init_app(app)

   @app.route('/')
   def home():
       return ':D'
   return app


if __name__ == "__main__":
   app = create_app()
   app.run(host='0.0.0.0', port=8004, debug=True)