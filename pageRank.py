import math, random, sys, csv 
from utils import parse, print_results

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'Expected input format: python pageRank.py <data_filename> <directed OR undirected>'
    else:
        filename = sys.argv[1]
        isDirected = False
        if sys.argv[2] == 'directed':
            isDirected = True

        graph = parse(filename, isDirected)

        for node in graph.nodes():
            print node + rank(graph, node)

            #neighbs = graph.neighbors(node)
            #print node + " " + str(neighbs)
            #print random.uniform(0,1)

def rank(graph, node):
    #V
    nodes = graph.nodes()
    #|V|
    nodes_sz = len(nodes) 
    #I
    neighbs = graph.neighbors(node)
    #d
    rand_jmp = random.uniform(0, 1)

    ranks = []
    ranks.append( (1/nodes_sz) )
    
    for n in nodes:
        rank = (1-rand_jmp) * (1/nodes_sz) 
        trank = 0
        for nei in neighbs:
            trank += (1/len(neighbs)) * ranks[len(ranks)-1]
        rank = rank + (d * trank)
        ranks.append(rank)

 

        
