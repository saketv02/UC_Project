##creates a dictionary of nodes and the number of circles they are a part of

import networkx as nx

def create_circle_dict(g):


    cirDict={}
    bip=nx.get_node_attributes(g,'bipartite');

    for node in g.nodes_iter():
        if (bip[node]==0):
            count=0
            for neighbor in g.neighbors(node):
                if(bip[neighbor]==1):
                    count=count+1
            cirDict[node]=count


    return cirDict

