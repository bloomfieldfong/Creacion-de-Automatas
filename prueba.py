import networkx as nx
import matplotlib.pyplot as plt
import random


def printGraph(G, pos):
    labels = nx.get_edge_attributes(G, 'weight')
    # positions for all nodes
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=300)
    # edges
    nx.draw_networkx_edges(G, pos, width=2)
    # labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.axis('off')
    plt.show()
    
    
