import networkx as nx
import readGraph
import nodeCircles
import operator
import SI
from collections import Counter

graph=readGraph.read()
dict=nodeCircles.create_circle_dict(graph)

sorted_dict=sorted(dict.items(),key=operator.itemgetter(1))  ##returns list of sorted dictionary
sorted_dict_reverse=sorted_dict[::-1]                        ##reverse list
epicurve=SI.spreadrumour(graph,0.1,100)                      #get spread of rumour

bip=nx.get_node_attributes(graph,'bipartite')   #get number of nodes of each class


print Counter(bip.values())
print graph.number_of_edges()
print graph.number_of_nodes()
print nx.get_node_attributes(graph,'bipartite')
print sorted_dict_reverse
print epicurve

