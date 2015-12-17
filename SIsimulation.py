import networkx as nx
import sys
import csv
import random
import sys
import csv
import operator


def spreadrumour(g,beta,seeds, outputFile):

    #Read the file into a graph
    G = g

    #Find the total number of nodes


    #Mark 5 nodes as infected
    numberOfNodesToInfect = seeds

    b = beta



    I = numberOfNodesToInfect #we seed the outbreak with one infectious individual
    S = 0 #this is the number of susceptibles


    #Now we're going to set the simulation clock to zero.
    t = 0

    susceptible = {}
    infected ={}
    newlyInfected = []

    print(numberOfNodesToInfect)

    bip=nx.get_node_attributes(g,'bipartite')

    #Infect some nodes at random
    count = 0
    for i in range(0,numberOfNodesToInfect):
        node = random.choice(G.nodes()) #assuming no same nodes are picked in choice
        if(bip[node] == 0):
            infected[node] = node


    sList = [] #we'll keep the number of susceptible individuals at each step on this list
    iList = [] #the number of infected individuals here
    #rList = [] #the number who have recovered here

    S = len(susceptible)
    I = len(infected)


    sList.append(S)
    iList.append(I)
    #rList.append(R)

    print(infected)
    print(S)
    print(I)

    infectedCircles = {}

    while I > 0:
        newlyInfected = {}


        #Find the susceptibles
        susceptible={}
        #Find the newly infected circles
        newlyInfectedCircles = {}
        for node in infected:
            neighbours = G.neighbors(node)
            for neighbour in neighbours:
                if(bip[neighbour] == 1):
                    if (neighbour not in newlyInfectedCircles) and (neighbour not in infectedCircles) :
                        newlyInfectedCircles[neighbour] = neighbour

        #Now the susceptibles are spreading through the circles.
        for newlyInfectedCircle in infectedCircles:
            for neighbor in G.neighbors(newlyInfectedCircle):
                if(bip[neighbor] == 0) and (neighbor not in susceptible) and (neighbor not in infected):
                    susceptible[neighbor] = neighbor




        S = len(susceptible)
        I = len(infected)

        print('------------------------Start with new susceptibles - Begin ---------------')
        print(S)
        print(I)
        print('------------------------Start with new susceptibles - - End---------------')

        #NEW PEOPLE ARE GETTING INFECTED
        newlyInfected = {}
        infected_num= int(round(b*len(susceptible)))
        print('Infecting ', infected_num ,'people now.')
        for i in range(0,infected_num):
            node=random.sample(susceptible,1)
            newlyInfected[node[0]] = node[0]
            del susceptible[node[0]]


        for i in newlyInfected:
            infected[i] = i

        for newlyInfectedCircle in newlyInfectedCircles:
            infectedCircles[newlyInfectedCircle] = newlyInfectedCircle

        S = len(susceptible)
        I = len(infected)
        #R = len(immune)

        #Then we add these values to their respective lists
        sList.append(S)
        iList.append(I)
        #rList.append(R)


        #This prints the time to standard out - usually the terminal you're running from -
        # and increments the timestep.
        t += 1
        if(t > 100):
            break


    w = csv.writer(open(outputFile, "wb"))
    for sus, inf in zip(sList, iList):
        w.writerow([sus, inf])

