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
import recursive_collapse 

import pygraphviz as pgv

"""
pgv has attribute functionality 
"""

path_dot = 'multiple_example_with_edge_labels.dot'

# Directed graph
G = pgv.AGraph(directed=True)

# Populate nodes and their values
G.add_node('A', value = 10)
G.add_node('B', value = 9)
G.add_node('C', value = 0)
G.add_node('D', value = 2)
G.add_node('E', value = 0)

# Populate edges and add their functions
G.add_edge('A','D', math = 'three_var')
G.add_edge('B','D', math = 'three_var')
G.add_edge('C','D', math = 'three_var')
G.add_edge('D','E', math = '+')

# Add edges labels
for edge in G.edges(): 
    a, b = edge[0], edge[1]
    G.get_edge(a,b).attr['label'] = ' ' + G.get_edge(a,b).attr['math']
    
# Write dot from pgv
G.layout(prog='dot')
G.write(path_dot)
G.draw('multiple_example_with_edge_labels.png')
G.draw('multiple_example_with_edge_labels.pdf')  

# Pick up dot into networkx for colapse 
"""
networkx has the ability to transform networks. 
"""
G = nx.drawing.nx_agraph.read_dot(path_dot)
math_dict = nx.get_edge_attributes(G,'math')
values_dict = nx.get_node_attributes(G,'value')
labels_dict = nx.get_edge_attributes(G,'label')

# Create a dictionaries: one with values, the next with functions 
math_dict = nx.get_edge_attributes(G,'math')
print('The math_dictionary is:')
print(math_dict)
values_dict = nx.get_node_attributes(G,'value')
print('The values_dict is:')
print(values_dict)

# Provide a map for strings to actual functions 
def three_var(a,b,c): 
    return a**2 + b**2 + c**2

calc_dict = {'+':np.add,
             '-':np.subtract,
             '*':np.multiply,
             '%':np.divide,
             'three_var':three_var}           

# We need to swap the order of our keys -- mathematical functions are order dependant! 
math_dict_sorted = {}
for key, math in math_dict.items():
    math_dict_sorted[tuple(reversed(key))] = math

math_dict = math_dict_sorted

# Run recursive function until all empty variables are complete.     
while len(math_dict) > 0:
    print(sorted(math_dict.items()))
    math_dict =  recursive_colapse.graph_colapse(math_dict, values_dict, calc_dict)