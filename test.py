import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import time
from FordFulkerson import *
from PPL import *

tFF = []
tS = []
y = []
for n in range(5,25):
    tmpTimeFF = []
    tmpTimeS = []
    for __ in range(10):
        array = np.random.randint(20, size=(n-1, n-1))
        m = np.append(array,[[0]*(n-1)], axis = 0)
        m = np.append(np.zeros((n,1)),m, axis = 1)
        for i in range(n):
            m[i,i] = 0

        G = nx.from_numpy_matrix(m, create_using=nx.DiGraph)
        print(m)
        #nx.draw(G,  with_labels = True)
        #plt.show()

        while nx.has_path(G,0,n-1) == False:
            array = np.random.randint(20, size=(n-1, n))
            m = np.append(array,[[0]*n], axis = 0)
            G = nx.from_numpy_matrix(m, create_using=nx.DiGraph)
        start_time = time.time()
        g = Graph(m)
        g.ford_fulkerson(0, n-1)
        tmpTimeFF.append(time.time()-start_time)

        start_time = time.time()
        mfsimplex(m)
        tmpTimeS.append(time.time()-start_time)
    tFF.append(sum(tmpTimeFF)/len(tmpTimeFF))
    tS.append(sum(tmpTimeS)/len(tmpTimeS))
    y.append(n)
print(tFF)
print(tS)
print(y)
plt.plot( y, tFF, label='FordFulkerson')
plt.plot( y, tS, label='Simplex')
plt.legend(loc='best')
plt.yscale('log')
plt.ylabel('Time (s)')
plt.xlabel('Nodes in the graph')
plt.title('Average processing time')
plt.savefig('com.png')
plt.show()
