def quarantine(graph, sorted_dict_reverse, nodesToQuarantine ):

    nodeRemoved = 0
    for nodeToQuarantine in sorted_dict_reverse:
        graph.remove_node(nodeToQuarantine[0])
        if(nodeRemoved >= nodesToQuarantine):
            break
        nodeRemoved = nodeRemoved + 1;


    return graph;