# Gmatch4py use networkx graph
import networkx as nx
import gmatch4py as gm
import matplotlib.pyplot as plt
# main.py
from appJar import gui
from os import path
import os


##file1= open('/Users/varlin/Desktop/fakefile.txt','rb')
##g1=nx.read_edgelist(file1,create_using=nx.Graph(),nodetype=int)
##file2= open('/Users/varlin/Desktop/fakefile1.txt','rb')
##g2=nx.read_edgelist(file2,create_using=nx.Graph(),nodetype=int)


def graphInfo(g1,g2):
    print("Graph 1 info: \n")
    print(nx.info(g1))
    print("Graph 2 Info: \n")
    print(nx.info(g2))
    information = nx.info(g1)
    print(type(information))

def plotGraphs(g1,g2):
    nx.draw(g1)
    plt.title("Graph 1")
    plt.show()

    nx.draw(g2)
    plt.title("Graph 2")
    plt.show()



def GEDx(g1,g2, dv, av, de, ae):
    ged = gm.GraphEditDistance(dv, av, de, ae)
    result = ged.compare([g1, g2], None)

    print("Raw Results:")
    print(result)
    return(result)

def GEDxbySimilarity(g1, g2, dv,av, de, ae):
        ged = gm.GraphEditDistance(dv,av, de, ae)
        result = ged.compare([g1, g2], None)
        print("Results normalized by similarity")
        print(ged.similarity(result))
        return(ged.similarity(result))


def GEDxbyDistance(g1, g2, dv,av, de, ae):
    ged = gm.GraphEditDistance(dv,av, de, ae)
    result = ged.compare([g1, g2], None)
    print("Results normalized by distance")
    print(ged.distance(result))
    return(ged.distance(result))

#Maximal Common Subgraph
def MCSX(g1,g2):

    maximal=gm.MCS()
    result=maximal.compare([g1,g2],None)
    print("Raw Results by Maximal Common SubGraph:")
    print(result)
    return(result)


#plotGraphs(g1,g2)
#GEDx(g1,g2)
#MCSX(g1,g2)

