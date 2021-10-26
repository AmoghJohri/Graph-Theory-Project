import random
import numpy             as     np
import networkx          as     nx
import matplotlib.pyplot as     plt 
from   point             import Point
from   line              import Line 

def getCustomGraph():
    # generate a custom graph
    G = nx.Graph()
    G.add_nodes_from(range(0, 15))
    G.add_edges_from([(0, 1), (0, 9), (0, 12), (0, 13)])
    G.add_edges_from([(1, 10), (1, 14)])
    G.add_edges_from([(2, 6), (2, 10)])
    G.add_edges_from([(4, 5), (4, 7), (4, 14)])
    G.add_edges_from([(5, 11)])
    G.add_edges_from([(6, 8)])
    G.add_edges_from([(7, 9), (7, 11), (7, 13), (7, 14)])
    G.add_edges_from([(8, 10)])
    G.add_edges_from([(9, 12)])
    G.add_edges_from([(11, 13)])
    G.add_edges_from([(12, 13)])
    return G 

def generateRandomGraph(n, p):
    # generate a random graph based on the number of nodes and the probability of an edge between each pair of  nodes
    G = nx.Graph()
    G.add_nodes_from(range(0, n))
    for i in G.nodes:
        for j in G.nodes:
            if i != j:
                if random.random() < p:
                    G.add_edge(i, j)
    return G

def generateRandomIntervalGraph(n, offset=100, giveIntervals = False):
    # generates random interval graphs
    intervals = []
    range_ = n*offset
    for i in range(n):
        val1 = random.randint(0, range_)
        val2 = random.randint(0, range_)
        intervals.append([min(val1, val2), max(val1, val2)])
    G = nx.Graph()
    G.add_nodes_from(range(0, n))
    for i in range(len(intervals)-1):
        for j in range(i+1, len(intervals)):
            if not (intervals[i][1] < intervals[j][0] or intervals[j][1] < intervals[i][0]):
                G.add_edge(i, j)
    if not giveIntervals:
        return G
    else:
        return G, intervals

def generateRandomPermutationGraph(n):
    parallelLine2 = [i for i in range(n)]
    random.shuffle(parallelLine2)
    lines = []
    iterator = 0
    for each in parallelLine2:
        lines.append(Line(Point(iterator, 0), Point(each, 1)))
        iterator += 1
    G = nx.Graph()
    G.add_nodes_from(range(0, n))
    for i in range(len(lines)-1):
        for j in range(i+1, len(lines)):
            if Line.isIntersecting(lines[i], lines[j]):
                G.add_edge(i, j)
    return G
    
def generateRandomComparabilityGraph(n, p):
    G = nx.Graph()
    G.add_nodes_from(range(0, n))
    for i in range(n-1):
        for j in range(i, n):
            if random.random() < p:
                G.add_edge(i, j)
    while True:
        tag = 0
        nodes = list(G.nodes)
        for each in nodes:
            N_each = list(G.neighbors(each))
            for neigh in N_each:
                NN_each = list(G.neighbors(neigh))
                for nneigh in NN_each:
                    if not G.has_edge(each, nneigh):
                        tag = 1
                        G.add_edge(each, nneigh)
        if tag == 0:
            break 
    return G

def getKnottingGraph(G):
    K_G = nx.Graph()
    nodes = list(G.nodes)
    offset = 10**(len(str(len(nodes))))
    connected_components = {}
    for node in nodes:
        connected_components[node] = list(nx.connected_components(nx.complement(G.subgraph(G.neighbors(node)))))
        K_G.add_nodes_from(range(node*offset, node*offset + len((connected_components[node]))))
    for edge in list(G.edges):
        u, v = edge
        i = 0
        while i < len((connected_components[u])):
            if v in (connected_components[u])[i]:
                break
            i += 1
        j = 0
        while j < len((connected_components[v])):
            if u in (connected_components[v])[j]:
                break
            j += 1
        K_G.add_edge(u*offset+i, v*offset+j)
    return K_G       
    
def generateRandomCoComparabilityGraph(n, p):
    return nx.complement(generateRandomComparabilityGraph(n, p))

def drawIntervals(I):
    iterator = 0
    for each in I:
        plt.plot([each[0], each[1]], [iterator, iterator])
        iterator += 1
    plt.legend(['Interval_' + str(i) for i in range(len(I))])
    plt.axis('off')
    plt.show()

def drawGraph(G):
    # draw the graph
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

def drawCustomGraph(G, color = [], colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k'], differentColors = False):
    # draw the graph along with the color
    nodes = list(G.nodes)
    pos   = {}
    edges = list(G.edges)
    diff  = 360/(len(nodes) + 1)
    for i in range(len(nodes)):
        x = np.cos(np.radians(i*diff))
        y = np.sin(np.radians(i*diff))
        pos[nodes[i]] = (x, y)
        if not differentColors:
            if nodes[i] in color:
                plt.plot(x, y, 'bo', markersize=8, color='r')
            else:
                plt.plot(x, y, 'bo', markersize=8)
        else:
            if len(color) > len(colors):
                plt.plot(x, y, 'bo', markersize=8)
            else:
                for j in range(len(color)):
                    if nodes[i] in color[j]:
                        plt.plot(x, y, 'bo', markersize=8, color=colors[j])
        plt.text(x + 0.03, y, nodes[i], fontsize=12)
    for each in edges:
        x_values = [pos[each[0]][0], pos[each[1]][0]]
        y_values = [pos[each[0]][1], pos[each[1]][1]]
        plt.plot(x_values, y_values, color='g')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edge(0, 1)
    G.add_edge(0, 3)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 3)
    drawCustomGraph(G)
