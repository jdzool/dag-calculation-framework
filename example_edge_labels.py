#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 21:43:40 2018

@author: jondowning
"""

import pygraphviz as pgv

"""
pgv has attribute functionality 
"""

path_dot = 'example_edge_labels.dot'

# Directed graph
G = pgv.AGraph(directed=True)

# Populate nodes and their functions
G.add_node('A', value = 1)
G.add_node('B', value = 1)
G.add_node('C', value = 1)
G.add_node('D', value = 1)
G.add_node('E', value = 1)

# Populate edges and their functions
G.add_edge('A','D', math = '+')
G.add_edge('B','D', math = '+')
G.add_edge('C','D', math = '+')
G.add_edge('D','E', math = '+')

for edge in G.edges(): 
    a, b = edge[0], edge[1]
    G.get_edge(a,b).attr['label'] = ' ' + G.get_edge(a,b).attr['math']
    
    
G.layout(prog='dot')
G.write(path_dot)

# Read dot file in networkx 

import networkx as nx


"""
networkx has the ability to transform networks. 
"""

G = nx.drawing.nx_agraph.read_dot(path_dot)
math_dict = nx.get_edge_attributes(G,'math')
values_dict = nx.get_node_attributes(G,'value')
labels_dict = nx.get_edge_attributes(G,'label')

nx.drawing.nx_agraph.write_dot(G, path_dot)

# Back to pygraphviz

"""
pgv has good plotting and DAG functionality 
"""

G=pgv.AGraph(path_dot) 
G.draw('example_edge_labels.png')