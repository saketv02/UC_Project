import networkx as nx
import readGraph
import nodeCircles
import operator
import SI
import SIsimulation
import QuarantineGraph
import SIR_new
import SIsimulationWithQuarantine
from collections import Counter

graph, dict =readGraph.read()
dict=nodeCircles.create_circle_dict(graph)

sorted_dict_reverse=sorted(dict.items(),key=operator.itemgetter(1), reverse = True)  ##returns list of sorted dictionary

#epicurve = SIsimulation.spreadrumour(graph,.1,100, 'normalFlow.csv')
#epicurve=SI.spreadrumour(graph,0.5,3000)                      #get spread of rumour
nodesToQuarantine = 100;
#quarantinedGraph = QuarantineGraph.quarantine(graph.copy(), sorted_dict_reverse, nodesToQuarantine)
#quarantinedEpicurve = SIsimulation.spreadrumour(quarantinedGraph,.1,10, 'quarantinedFlow.csv')

epicurve = SIR_new.spreadrumour(graph,.1,0.2,10, sorted_dict_reverse, 'recover10.csv',10)

# bip=nx.get_node_attributes(graph,'bipartite')   #get number of nodes of each class
#
#
# print Counter(bip.values())
# print graph.number_of_edges()
#print graph.number_of_nodes()

# print nx.get_node_attributes(graph,'bipartite')
# print sorted_dict_reverse
#print (epicurve)

