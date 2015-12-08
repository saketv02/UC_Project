import networkx as nx
import readGraph
import nodeCircles
import operator
import SI
import SIsimulation
import QuarantineGraph
import SIsimulationWithQuarantine
from collections import Counter

graph, dict =readGraph.read()
dict=nodeCircles.create_circle_dict(graph)

sorted_dict_reverse=sorted(dict.items(),key=operator.itemgetter(1), reverse = True)  ##returns list of sorted dictionary

#epicurve = SIsimulation.spreadrumour(graph,.1,100, 'normalFlow.csv')
#epicurve=SI.spreadrumour(graph,0.5,3000)                      #get spread of rumour
nodesToQuarantine = 400;
#quarantinedGraph = QuarantineGraph.quarantine(graph.copy(), sorted_dict_reverse, nodesToQuarantine)
#quarantinedEpicurve = SIsimulation.spreadrumour(quarantinedGraph,.1,100, 'quarantinedFlow.csv')

epicurve = SIsimulationWithQuarantine.spreadrumour(graph,.5,500, sorted_dict_reverse, 'secondDegreeQuarantine.csv')

# bip=nx.get_node_attributes(graph,'bipartite')   #get number of nodes of each class
#
#
# print Counter(bip.values())
# print graph.number_of_edges()
print graph.number_of_nodes()

# print nx.get_node_attributes(graph,'bipartite')
# print sorted_dict_reverse
print (epicurve)

