import networkx as nx


def read():

    graph=nx.Graph()

    egoNode=['0','107','348','414','686','698','1684','1912','3437','3980']

    #create edgelist for all files
    isCircle = 'bipartite'

    for node in egoNode:
        with open('facebook/'+node+'.edges',mode='rU') as f:
            for line in f:
                line= line.strip('\n')
                val= line.split(' ')
                if(val[0]!=' '):
                    graph.add_edge(val[0],val[1])
                    graph.add_edge(node,val[0])
                    graph.add_edge(node,val[1])
                    graph.node[val[0]][isCircle]=0
                    graph.node[val[1]][isCircle]=0
        graph.node[node][isCircle]=0

    cirDict={}

    #create circles
    for node in egoNode:
        with open('facebook/'+node+'.circles',mode='rU') as f:
            count=0
            for line in f:
                line =line.strip('\n')
                val = line.split('\t')
                if(val[0]!=' '):
                    #print "length",val,node

                    count=count+1
                    cirDict[node+'circle'+str(count)]= len(val)
                    for i in range(1,len(val)):
                        graph.add_edge(node+'circle'+str(count),val[i])
                        graph.node[val[i]][isCircle]=0
                        graph.node[node+'circle'+str(count)][isCircle]=1
                         #print "read value",val[i]
                graph.add_edge(node+'circle'+str(count),node)

    return graph, cirDict
