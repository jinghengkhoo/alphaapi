import logging

import config
from api.scraper import scrape
from flask_cors import cross_origin
from flask import request
from flask_restful import Api, Resource

api = Api(prefix=config.API_PREFIX)

logger = logging.getLogger()

class SyncProcessAPIView(Resource):
   """POST API class"""
   @cross_origin()
   def post(self):
      """
      (POST)
      upload: <urlstr/image>
      returns quant data from list of tickers
      """
      logger.info('New Request')
      data = request.form
      if not "ticker" in data:
        return ":(", 200

      ratings = scrape(data["ticker"])

      return {"ratings": ratings}, 200

api.add_resource(SyncProcessAPIView, '/rate')