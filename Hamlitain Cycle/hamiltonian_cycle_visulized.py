# Prints all the hamiltonian paths possible for a given undirected graph

import numpy as np
import networkx as nx
from timeit import default_timer as timer
from matplotlib import pyplot as plt


graph = [];
NODES = 0
PATH = []


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

    # displayCycle()
    return True



def plot_complexity(func, stop):
  title = "Hamiltonian Cycle Problem"
  data = {
      'length of list':[],
      'time taken': []
  }

  for i in range(3, stop):
      # creating new graph & setting the global vars
      global graph, NODES, PATH

      temp = np.random.randint(low = 0, high= 2, size = (i,i), dtype = int)
      graph = temp.tolist()
      NODES = i
      PATH = []

      start = timer()
      func()
      end = timer()

      print(f'Hamiltonian Problem for graph of {i} nodes solved in {end-start}s')

      data['length of list'].append(i)
      data['time taken'].append(end-start)

  plt.plot(data['length of list'], data['time taken'], label=title)
  plt.title(title)
  plt.xlabel('Size of matrix')
  plt.ylabel('Time taken')
  plt.show()


if __name__ == "__main__":
  plot_complexity(hamiltonianCycle, 500)
