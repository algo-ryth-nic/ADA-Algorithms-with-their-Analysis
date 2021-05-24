from timeit import default_timer as timer
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

# TODO: compare with kruskal algo...
# also compare with sparse and dense algos for both algos
# error when given a sparse graph, i.e. when a disjoint node is encountered

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        print(self.V)
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]

    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])


    def getMST(self, parent):
        edge_list = []
        for i in range(1, self.V):
            edge_list.append((parent[i], i))
        return edge_list


    def minKey(self, key, mstSet):
        # Initilaize min value, a large value INT_MAX
        min = 99999999

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index


    # Function to construct and print MST for a graph represented using adjacency matrix representation
    def primMST(self, print_output= True):
        # Key values used to pick minimum weight edge in cut
        key = [99999999] * self.V
        parent = [None] * self.V # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1 # First node is always the root of

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):

                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u

        if print_output:
            self.printMST(parent)

        return self.getMST(parent)


def generate_random_graph(n, random_weights = True):
    """
    Parameter: n = No. of nodes

    Uses networkx's graph generator to create a random graph
    which is then turned to a numpy 2d matrix (adjacency matrix)
    this matrix is then converted to python's 2d list type
    this is then returned
    """
    Graph = nx.fast_gnp_random_graph(n, 1)

    if(random_weights):
        for (u, v) in Graph.edges():
            Graph.edges[u,v]['weight'] = np.random.randint(1,999, dtype=int)

    # in numpy
    graph = nx.to_numpy_matrix(Graph)
    # to list
    graph = graph.tolist()

    return graph


def draw_graph(graph):
    # drawing onto canvas
    nx.draw(graph, with_labels = True, edge_color = 'black' ,width = 1, alpha = 0.95)
    # showing diagram
    plt.show()


# using adjency matrix, O(V^2)
def plot_complexity(stop):
  title = f"Prims Algorithm O(V^2)"
  data = {
      'length of list':[],
      'time taken': []
  }

  # main loop
  for i in range(2, stop+1):
    # setting the no. of nodes for graph
    G = Graph(i)

    # generating the random graph with a edge creation probability of 1 (dense graph)
    G.graph = generate_random_graph(i)

    start = timer()
    edge_list = G.primMST(print_output= False)
    end = timer()

    print(f"MST edges-list: {edge_list}")
    print(f'Find the MST using Prims Algorithm for graph of {i} nodes solved in {end-start} s')

    data['length of list'].append(i)
    data['time taken'].append(end-start)

  plt.plot(data['length of list'], data['time taken'], label=title)
  plt.title(title)
  plt.xlabel('Size of graph')
  plt.ylabel('Time taken')
  plt.show()


def main():

    V = 5
    G = Graph(V)

    # default example
    G.graph = [ [0, 2, 0, 6, 0],
                [2, 0, 3, 8, 5],
                [0, 3, 0, 0, 7],
                [6, 8, 0, 0, 9],
                [0, 5, 7, 9, 0]]

    # G.graph = generate_random_graph(V)
    print("Printing Original graph\n")
    g = nx.Graph()
    g = nx.from_numpy_matrix(np.array(G.graph))
    draw_graph(g)

    edge_list = G.primMST()

    print(edge_list)

    # Drawing MST
    print("Printing MST graph\n")
    g = nx.Graph()
    g.add_edges_from(edge_list)
    draw_graph(g)



if __name__ == "__main__":
    # main()
    plot_complexity(stop = 100)

