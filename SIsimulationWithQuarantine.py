import networkx as nx
import sys
import csv
import random
import sys
import csv
import operator


def spreadrumour(g,beta,seeds,sorted_dict_reverse, outputFile):

    #Read the file into a graph
    G = g

    #Find the total number of nodes


    #Mark 5 nodes as infected
    numberOfNodesToInfect = seeds

    b = beta

    immunizationBudget = 1;

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

    infectedGroups = {}
    susceptibleGroupList = {}

    #We begin with the assumption that the seed nodes have contaminated the groups that they are part of.
    for node in infected:
            neighbours = G.neighbors(node)
            for group in neighbours:
                if(bip[group] == 1):
                    if (group not in infectedGroups) :
                        infectedGroups[group] = group

    while I > 0:
        newlyInfected = {}


        #Find the susceptibles
        susceptible={}
        #Find the newly infected groups
        newlyInfectedGroups = {}
        for node in infected:
            neighbours = G.neighbors(node)
            for group in neighbours:
                if(bip[group] == 1):
                    if (group not in newlyInfectedGroups) and (group not in infectedGroups) :
                        newlyInfectedGroups[group] = group
                        if group in susceptibleGroupList:
                            del susceptibleGroupList[group]



        #Get all the NODES ONLY for this group. These members are susceptible to the infection. Add them to the susceptible list.
        for newlyInfectedGroup in infectedGroups:
            for member in G.neighbors(newlyInfectedGroup):
                if(bip[member] == 0) and (member not in susceptible) and (member not in infected):
                    susceptible[member] = member
                    #Find the groups this particular node is part of, and add it to the susceptible group list.
                    for group in G.neighbors(member):
                        if(bip[group] == 1) and (group not in susceptibleGroupList) and (group not in infectedGroups):
                            susceptibleGroupList[group] = group


        processingList = {}
        #Now we have a susceptibleGroupList.
        #Walk through all susceptible groups.
        for susceptibleGroup in susceptibleGroupList: #Guaranteed to be a group
            #Check if only  one unique node out of susceptible and infected is present in the group's members.
            uniqueSusceptibleCount = 0;
            onlyMember = ''
            for member in G.neighbors(newlyInfectedGroup):
                if(bip[member] == 0):
                    if(member in susceptible) and (member not in infected):
                        uniqueSusceptibleCount = uniqueSusceptibleCount + 1
                        onlyMember = member
            if  uniqueSusceptibleCount <= 1:
                if(len(onlyMember) > 0):
                    processingList[onlyMember] = len(G.neighbors(susceptibleGroup)) #This group is guaranteed to have only one susceptible. Add it
            #del susceptibleGroupList[susceptibleGroup]

        #If the processing list is empty, still clear out based on best hunch.
        if len(processingList) < 1:
            nodeRemoved = 0
            for nodeToQuarantine in sorted_dict_reverse:
                if G.has_node(nodeToQuarantine[0]):
                    G.remove_node(nodeToQuarantine[0])
                    if(nodeToQuarantine[0] in infected):
                        del infected[nodeToQuarantine[0]]
                    if(nodeToQuarantine[0] in susceptible):
                        del susceptible[nodeToQuarantine[0]]
                    if(nodeRemoved >= immunizationBudget):
                        break
                    nodeRemoved = nodeRemoved + 1;

        sortedProcessingList = sorted(processingList.items(),key=operator.itemgetter(1), reverse = True)

        #Remove the 1 most potential lethal node:
        lethalNodeRemovalCount = 0;
        for lethalNodes in sortedProcessingList:
            G.remove_node(lethalNodes[0])
            if node in susceptible:
                del susceptible[lethalNodes[0]]
            print('----------- Removed lethal node --- ', lethalNodes[0] , '. It had degree', lethalNodes[1])
            lethalNodeRemovalCount = lethalNodeRemovalCount + 1
            if(lethalNodeRemovalCount >= immunizationBudget):
                break

        S = len(susceptible)
        I = len(infected)

        print('------------------------Start with new susceptibles - Begin ---------------')
        print(S)
        print(I)
        print('------------------------Start with new susceptibles - - End---------------')

        #NEW PEOPLE ARE GETTING INFECTED
        newlyInfected = {}
        infected_num= int(round(b*len(susceptible)))
        for i in range(0,infected_num):
            node=random.sample(susceptible,1)
            newlyInfected[node[0]] = node[0]
            del susceptible[node[0]]


        for i in newlyInfected:
            infected[i] = i

        for newlyInfectedGroup in newlyInfectedGroups:
            infectedGroups[newlyInfectedGroup] = newlyInfectedGroup

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
        if(t > 50):
            break


    w = csv.writer(open(outputFile, "w"))
    for sus, inf in zip(sList, iList):
        w.writerow([sus, inf])

