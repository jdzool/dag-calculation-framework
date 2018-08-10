#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:49:19 2017

@author: jondowning
"""
import networkx as nx
import numpy as np
from networkx.drawing.nx_pydot import write_dot
import pygraphviz as pgv
import pandas as pd 
import recursive_colapse 

# Load inputs! 

# Create a directed network 
# Calculations have a specific direction 
G = pgv.AGraph(directed=True)

# Populate nodes and their values 
G.add_node('A', attr_dict={'value':5})
G.add_node('B', attr_dict={'value':2})
G.add_node('C', attr_dict={'value':3})
G.add_node('D', attr_dict={'value':4})
G.add_node('E', attr_dict={'value':0})

# Populate edges and their functions
G.add_edge('A','B', attr_dict={'math':'+'})
G.add_edge('B','C', attr_dict={'math':'-'})
G.add_edge('D','E', attr_dict={'math':'+'})
G.add_edge('C','E', attr_dict={'math':'+'})

# Add edge labels -- the same as the math labels 
for edge in G.edges(): 
    a, b = edge[0], edge[1]
    G.get_edge(a,b).attr['label'] = G.get_edge(a,b).attr['math']

# Provide a map for strings to actual functions 
calc_dict = {'+':np.add,
             '-':np.subtract,
             '*':np.multiply,
             '%':np.divide}           

# Create a dictionaries: one with values, the next with functions 
math_dict = nx.get_edge_attributes(G,'math')
print(math_dict)
values = nx.get_node_attributes(G,'value')

# We need to swap the order of our keys -- mathematical functions are order dependant! 
math_dict_sorted = {}
for key, math in math_dict.items():
    math_dict_sorted[tuple(reversed(key))] = math

math_dict = math_dict_sorted

# Run recursive function until all empty variables are complete.     
while len(math_dict) > 0:
    print(sorted(math_dict.items()))
    math_dict = recursive_colapse.graph_colapse(math_dict)
    
# Saving output and draw 
dot_path = "example_graph.dot"

# Write .dot file to local drive 
write_dot(G,dot_path)

# Export visualisation 
# Edge attributes are not visualised but this is possible 
V = pgv.AGraph(dot_path)
V.layout(prog='dot')
V.draw('linear_example_pgv.png')
V.draw('linear_example_pgv.pdf')   
