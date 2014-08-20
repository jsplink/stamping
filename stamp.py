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

# sets = [
#   [[795,1411],[854,568],[696,328],[141,1138],[238,276]],
#   [[733,1372],[903,748],[783,487],[117,1209],[335,358]],
#   [[430,1368],[668,1134],[558,547],[794,779],[312,894]],
#   [[870,937],[628,692],[64,801],[275,565],[386,1046]],
#   [[526,650],[102,857],[781,794],[482,1648],[1044,1374]],
#   [[728,1422],[762,779],[587,701],[89,1389],[133,508]],
#   [[116,889],[126,1227],[638,1547],[300,1558],[534,1127]],
#   [[320,888],[339,1229],[857,1537],[517,1557],[744,1121]],
#   [[817,1040],[771,399],[579,572],[178,1078],[108,205]],
#   [[874,1312],[792,677],[594,456],[239,1394],[130,513]],
#   [[890,1181],[654,940],[74,1064],[303,831],[423,1304]],
#   [[990,906],[781,646],[187,703],[439,488],[516,980]],
#   [[869,938],[627,693],[63,800],[276,566],[385,1047]],
#   [[785,160],[335,110],[951,413],[241,985],[883,1055]],
#   [[92,787],[355,990],[926,804],[722,1065],[541,610]],
#   [[41,776],[286,976],[855,767],[652,1040],[474,581]],
#   [[494,344],[62,494],[733,500],[344,1327],[947,1116]],
#   [[702,369],[244,338],[863,622],[167,1207],[810,1265]],
#   [[91,853],[736,848],[969,661],[86,209],[964,203]],
#   [[892,1047],[879,700],[364,400],[703,375],[470,809]],
#   [[64,1125],[698,1149],[934,980],[86,474],[956,514]],
#   [[464,318],[1007,649],[134,868],[165,1157],[569,1406]],
#   [[439,397],[1009,680],[128,983],[233,1067],[652,1471]],
#   [[301,137],[935,266],[180,779],[316,1038],[771,1128]],
#   [[64,605],[661,416],[211,1218],[478,1345],[924,1249]],
#   [[796,1360],[740,1031],[199,778],[532,720],[346,1177]],
#   [[193,1128],[538,1083],[806,551],[852,877],[402,682]],
#   [[0,1135],[254,1343],[822,1144],[622,1418],[441,953]],
#   [[119,719],[363,937],[943,792],[724,1039],[585,563]],
#   [[53,896],[296,1103],[870,913],[662,1180],[492,716]]
# ]
