# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_path([1,2,3],color='red')
color=nx.get_edge_attributes(G,'color')

nx.draw(G, cmap = plt.get_cmap('jet'))
plt.show()