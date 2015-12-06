import networkx as nx
import random


def spreadrumour(g,beta,seeds):

    tMax=100 #time steps for simulation
    infect={}  #infected people
    epicurve=list()
    bip=nx.get_node_attributes(g,'bipartite')

##plant seeds

    for i in range(0,seeds):
        while True:
            node = random.choice(g.nodes())
            if(bip[node]==0):
                infect[node]=0
                break

    epicurve.append(len(infect))

### spread infection

    for i in range(0,tMax):
        suscept={}      #susceptible


        for node in infect:
            #create list of susceptible nodes

            #first find circles node belongs to
            circles=list()
            for neighbour in g.neighbors(node):
                if(bip[neighbour]==1):
                    circles.append(neighbour)

            #add everyone in circle to susceptible list
            for circle in circles:
                for neighbour in g.neighbors(circle):
                    if(bip[neighbour]==0) and neighbour not in infect:
                        suscept[neighbour]=0

        #time to infect
        infected_num=int(round(beta*len(suscept)))

        for i in range(0,infected_num):
            node=random.sample(suscept,1)
            infect[node[0]]=0
            del suscept[node[0]]

        #update epicurve
        epicurve.append(len(infect))

    return epicurve



