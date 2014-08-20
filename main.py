from stamp import Stamp
import webapp2
import logging
from logging import config as logging_config
from settings import LOGGING
logging_config.dictConfig(LOGGING)
logging = logging.getLogger('default')
class BaseHandler(webapp2.RequestHandler):

  ###############################
  '''  First Level Dispatch   '''
  ###############################

  def dispatch(self):
    logging.info('[DISPATCH] ( %s ) %s' % (self.request.remote_addr, self.request.query))
    try:
      # Dispatch the request.
      webapp2.RequestHandler.dispatch(self)
    except Exception as e:
      logging.error(e)

class StampHandler(BaseHandler):
  def get(self):
    if "dots" in self.request.params:
      dots = self.request.params.get('dots')
    try:
      dots = dots.split(',')
      STAMP_A = [[238,276],[698,324],[853,574],[148,1146],[786,1215]]
      test_config = []
      while dots:
        test_config.append([dots.pop(0), dots.pop(0)])
      stamp_a = Stamp(STAMP_A)
      self.response.status_int == 200
      if stamp_a.test(test_config):
        self.response.write('A\n')
      else:
        self.response.write('_\n')
    except Exception as e:
      logging.error(e)
