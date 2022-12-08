import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import time
import scipy as sp
from scipy.optimize import linprog
start_time = time.time()
m = np.array([[0,11,9,0],
    [0,0,1,3],
    [0,16,0,19],
    [0,0,0,0]])

def mfsimplex(m):
    n = len(m)
    A = []
    G = nx.from_numpy_matrix(m, create_using=nx.DiGraph)
    b = []
    c = []#-m[:,-1]/m[:,-1]# Ya esta

    #c[np.isnan(c)] = 0
    edges = list(G.edges(data=True))
    
    en = len(edges)
    A = []
    B = []

    for i in range(en):
        B.append(edges[i][2]['weight'])
        tmp = [0]*en
        tmp[i] = 1
        A.append(tmp)

    for i in G.nodes:
        if i != 0 and i != n-1:
            tmp = [0]*en
            outEdges = G.out_edges([i],data= True)
            inEdges = G.in_edges([i],data= True)
            for e in inEdges:
                 tmp[edges.index(e)] = 1

            for e in outEdges:
                 tmp[edges.index(e)] = -1

            A.append(tmp)
            B.append(0)
        elif i == n-1:
            inEdges = G.in_edges([i],data= True)
            for e in inEdges:
                 tmp[edges.index(e)] = 1
            c=tmp

    b = B
    bounds = [(0, None)]

    res = linprog(c, A_ub=A, b_ub=b,  bounds=bounds, method='simplex', options={"disp": True})
    return res

if __name__ == '__main__':
    print(mfsimplex(m))
