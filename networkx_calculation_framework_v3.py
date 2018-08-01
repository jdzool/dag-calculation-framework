#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:49:19 2017

@author: jondowning

Example of how graphical networks could be used for a calculation framework
Grpahical engine = networkx
Visualisation and plotting = pygraphviz
"""

import networkx as nx
import numpy as np
from networkx.drawing.nx_pydot import write_dot
import pygraphviz as pgv
import pandas as pd 





G = nx.DiGraph()

# Populate nodes 
G.add_node('A', attr_dict={'value':5})
G.add_node('B', attr_dict={'value':2})
G.add_node('C', attr_dict={'value':3})
G.add_node('D', attr_dict={'value':4})
G.add_node('E', attr_dict={'value':0})

# Populate edges 
G.add_edge('A','C', attr_dict={'math':'+'})
G.add_edge('B','C', attr_dict={'math':'-'})
G.add_edge('D','E', attr_dict={'math':'+'})
G.add_edge('C','E', attr_dict={'math':'+'})

math_dict = nx.get_edge_attributes(G,'math')
values = nx.get_node_attributes(G,'value')

# Calculation dictionary
calc_dict = {'+':np.add,
             '-':np.subtract,
             '*':np.multiply,
             '%':np.divide}

# TO DO provide abstraction to Excel              

# We need to swap the order of our keys -- mathematical functions are order dependant! 
math_dict_sorted = {}
for key, math in math_dict.items():
    math_dict_sorted[tuple(reversed(key))] = math

math_dict = math_dict_sorted

# Recursive function     
def graph_colapse(math_dict):
    # List to remove 
    to_pop = {}
    
    # Note: The order of mathematical functions is important  
    # This is a unique problem but has been solved 
    # Here simplistically we can use an alphabetical sort 
    # NB: we could use a topological sorting function here
    for key, math in sorted(math_dict.items()):
        val_list = [values[x] for x in key]

        if list(values.values()).count(0) == 1:
            last = True
        else:
            last = False

        if all(val_list) or last:
            print('Processing edge: %s' %str(key))
            print('Initial node value: %s = %s' %(key[0], values[key[0]]))
            print('Node values are: %s' %(val_list))
            print('Edge function is %s' %math)
            
            values[key[0]] = calc_dict[math](*val_list)
            print('Updated node value: %s = %s' %(key[0], values[key[0]]))
            # Which items have been calculated 
            to_pop[key] = math

    # Remove edges which have been calculated 
    for key, math in to_pop.items():
        math_dict.pop(key, math)
        
    return math_dict

# Run recursive function until all empty variables are complete.     
while len(math_dict) > 0:
    print(sorted(math_dict.items()))
    math_dict = graph_colapse(math_dict)

# TODO Get functions written on edges 




# Saving output and draw 
dot_path = "example_graph.dot"

# Write .dot file to local drive 
write_dot(G,dot_path)

# Export visualisation 
# Edge attributes are not visualised but this is possible 
V = pgv.AGraph(dot_path)
V.layout(prog='dot')
V.draw('simple.png')
V.draw('simple.pdf')   
    

    
    
    
    
    
    
    
    