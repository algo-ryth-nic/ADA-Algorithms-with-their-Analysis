# Prints all the hamiltonian paths possible for a given undirected graph

import numpy as np
import networkx as nx
from timeit import default_timer as timer
from matplotlib import pyplot as plt


graph = [
   [0, 1, 0, 1, 0],
   [1, 0, 1, 1, 1],
   [0, 1, 0, 0, 1],
   [1, 1, 0, 0, 1],
   [0, 1, 1, 1, 0],
];

NODES = len(graph)
PATH = [];


def displayCycle():
    '''
    Prints the array path, which contains one of the hamiltonian paths
    to complete the path we append the first element
    '''
    PATH.append(PATH[0])
    print(f"Cycle: {PATH}")


def isValid(v, k):
   if graph [ PATH[k-1] ][v] == 0:          # no edge present :(
      return False

   for i in range(0, k):
      if PATH[i] == v:
         return False
   return True


def cycleFound(k):
    if k == NODES:
        if graph[PATH[k-1]][ PATH[0] ] == 1:
            return True
        else:
            return False


    for v in range(1, NODES):
        if isValid(v,k):
            PATH[k] = v
            if cycleFound (k+1) == True:
                return True
            PATH[k] = -1

    return False


def hamiltonianCycle():
    for i in range(0, NODES):
        PATH.append(-1)
    PATH[0] = 0

    if cycleFound(1) == False:
        print("Solution does not exist")
        return False

    displayCycle()
    return True


def main():
   hamiltonianCycle();


if __name__ == "__main__":
    start = timer()
    main()
    end = timer()

    # print(f"[Time Taken] {end-start}s")
    print(f"\n[Time Taken] {(end-start)*10**3}ms")

    # G = nx.Graph()
    graph = np.array(graph)
    G = nx.from_numpy_matrix(graph)

    # nx.draw(G)
    # nx.draw(G, with_labels = True, edge_color = ('r', 'b', 'g', 'y') ,width = 1, alpha = 1)

    nx.draw(G, with_labels = True, edge_color = 'black' ,width = 1, alpha = 0.8)
    plt.show()
