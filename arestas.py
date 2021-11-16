import networkx as nx
import matplotlib.pyplot as plt

#Grafo G
G = nx.read_edgelist("arestas.txt",delimiter=',')
#Gera o complementar do grafo G
GC = nx.complement(G)

nx.draw(GC, node_color='green', node_size=1500)
plt.show()

'''
for clq in nx.clique.find_cliques(G):
    print(clq)
'''
