import webapp2
import stamp
from main import StampHandler
from paste import httpserver
REMOTE = True

import logging
from logging import config as logging_config
from settings import LOGGING
logging_config.dictConfig(LOGGING)
logging = logging.getLogger('default')
config = {
  'webapp2_extras.sessions': {
    'secret_key': 'fjwp89eahf89ewh8f97h389fh89warh3waoeiwaj'
  }
}

application = webapp2.WSGIApplication([
  webapp2.Route('/snowshoe', handler=StampHandler)
], debug=True, config=config)

