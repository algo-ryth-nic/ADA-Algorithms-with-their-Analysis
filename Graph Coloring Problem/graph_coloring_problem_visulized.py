# Graph Coloring Decision Problem / m coloring problem

from timeit import default_timer as timer
import networkx as nx
from matplotlib import pyplot as plt
import numpy as np


class Graph():
    def __init__(self, graph):
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

    # A recursive utility function to solve m
    # coloring  problem
    def graphColourUtil(self, m, colour, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColourUtil(m, colour, v + 1) == True:
                    return True
                colour[v] = 0


    def graphColouring(self, m):
        color = [0] * self.V
        if self.graphColourUtil(m, color, 0) == None:
            print("No solution")
            return False

        # Print the solution
        print( "Solution exist and Following are the assigned colours:")

        print(color)



def generate_random_graph(n):
    Graph = nx.fast_gnp_random_graph(n, 0.4)
    # in numpy
    graph = nx.to_numpy_matrix(Graph)
    # to list
    graph = graph.tolist()

    return graph


# color_nb^nodes ... 3^n
def plot_complexity(color_nb, stop):
    title = f"Graph Coloring Problem / M-Coloring Problem ({color_nb}^n)"
    data = {
        'length of list':[],
        'time taken': []
    }

    for i in range(color_nb+1, stop+1):
        # Creating graph
        G = Graph(generate_random_graph(i))

        start = timer()
        G.graphColouring(color_nb)
        end = timer()

        print(f'M-Coloring Problem for graph of {i} nodes solved in {end-start}s')

        data['length of list'].append(i)
        data['time taken'].append(end-start)

    plt.plot(data['length of list'], data['time taken'], label=title)
    plt.title(title)
    plt.xlabel('Size of matrix')
    plt.ylabel('Time taken')
    plt.show()


if __name__ == "__main__":
    # number of colors
    color_nb = 3

    plot_complexity(color_nb, 30)
