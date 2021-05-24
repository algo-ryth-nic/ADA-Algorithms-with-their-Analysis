# Graph Coloring Decision Problem / m coloring problem

from timeit import default_timer as timer
import networkx as nx
from matplotlib import pyplot as plt
import numpy as np

# Graph class
class Graph():

    # constructor method
    def __init__(self, graph):
        """
        Parameters: A 2d list that represents the graph (adjacency matrix)
        creates two class members 'graph' and V (total no. of vertices)
        """
        self.graph = graph
        self.V = len(graph)


    # A utility function to check
    # if the current color assignment
    # is safe for vertex v
    def isSafe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True


    # A recursive helper method to solve m-coloring problem
    def graphColourUtil(self, m, colour, v):
        '''
        Takes no. of colors, color array and vertex
        returns True if solution is found
        else None
        '''
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColourUtil(m, colour, v + 1) == True:
                    return True
                colour[v] = 0


    # Method to check if graph satifies m-coloring problem
    def graphColouring(self, m):
        """
        Takes no. of colors
        returns all the colors found if solution is found
        else, returns False
        """
        color = [0] * self.V
        if self.graphColourUtil(m, color, 0) == None:
            print("No solution")
            return False

        # Print the solution
        print(f"Solution exist!!\nColors Assigned:{color}")

        return color


def generate_random_graph(n):
    """
    Parameter: n = No. of nodes

    Uses networkx's graph generator to create a random graph
    which is then turned to a numpy 2d matrix (adjacency matrix)
    this matrix is then converted to python's 2d list type
    this is then returned
    """
    Graph = nx.fast_gnp_random_graph(n, 0.5)
    # in numpy
    graph = nx.to_numpy_matrix(Graph)
    # to list
    graph = graph.tolist()

    return graph


if __name__ == "__main__":
    # Our graph
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]

    # to use a random graph instead
    # graph = generate_random_graph(nodes)
    g = Graph(graph)
    g.graph = graph

    # number of colors
    m = 3

    # timing the problem
    start = timer()
    colors = g.graphColouring(m)
    end = timer()

    print(f'[TIME-TAKEN] {(end-start)*10**3} ms')

    # when no solution is found
    if colors == False:
        exit(0)

    # our color pallet
    default_Colors = ["green", "blue", "yellow", "pink", "red", "black", "gray", "brown", "orange", "plum"]

    # mapping with color pallet
    node_colors = [default_Colors[i-1] for i in colors]

    # converting to networkx obj
    G = nx.from_numpy_matrix(np.array(graph))

    # drawing onto canvas
    nx.draw(G, with_labels = True, node_color= node_colors, edge_color = 'black' ,width = 1, alpha = 0.95)

    # showing diagram
    plt.show()


