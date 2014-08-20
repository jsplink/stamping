import timeit
from igraph import *

import logging
from logging import config as logging_config
from settings import LOGGING
logging_config.dictConfig(LOGGING)
logging = logging.getLogger('default')

def distance(p1, p2):
  return ((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2) ** 0.5

class Stamp():
  def __init__(self, points):
    # create graph with N points
    self.g = Graph([(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)])

    # add x and y to the graph nodes
    self.g.vs["x"] = [int(i[0]) for i in points]
    self.g.vs["y"] = [int(i[1]) for i in points]
    
    # get the point-to-point connections
    self.layout = Layout(zip(self.g.vs["x"], self.g.vs["y"]))

    # calculate the distance weighting 
    weights = [distance(self.layout[edge.source], self.layout[edge.target]) for edge in self.g.es]
    self.g.es["weight"] = weights

    # grab the maximum distance
    max_weight = max(weights)

    # set the width attr relative to the maximum dist.
    self.g.es["width"] = [6 - 5*weight/max_weight for weight in weights]

    # generate the MST
    self.mst = self.g.spanning_tree(weights)
    
  def plot(self):
    fig = Plot()
    fig.add(self.g, layout=self.layout, opacity=0.25, vertex_label=None, edge_label=self.g.es["weight"])
    fig.add(self.mst, layout=self.layout, edge_color="red", vertex_label=None)
    fig.show()

  def test(self, point_set, plot=False, TERROR=20):
    # grab the stamp's distances
    stamp_weights = sorted(self.g.es["weight"])
    matches = []
    test = Stamp(point_set)

    # grab the weights and test them
    test_weights = sorted(test.g.es["weight"])
    matched_weights = [stamp_weights[i] <= test_weights[i] + TERROR and stamp_weights[i] >= test_weights[i] - TERROR for i in range(len(test_weights))]

    # check if all distances match
    if matched_weights.count(True) == len(test_weights):
      if plot:
        test.plot()
      return True
    else:
      return False

def benchmark(points):
  STAMP_A = [[238,276],[698,324],[853,574],[148,1146],[786,1215]]
  stamp = Stamp(STAMP)
  result = stamp.test(points)

def benchmark_test():
  # timing the loops
  n = int(raw_input('how many times to test?'))
  cost = timeit.timeit('benchmark([[795,1411],[854,568],[696,328],[141,1138],[238,276]])', setup="from __main__ import test", number=n)
  logging.info('seconds: ' + str(cost))
