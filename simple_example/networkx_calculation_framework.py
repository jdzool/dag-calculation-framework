#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:49:19 2017

@author: jondowning
"""

import networkx as nx
import numpy as np

G = nx.DiGraph()

# Populate nodes 
G.add_node('A', attr_dict={'value':5})
G.add_node('B', attr_dict={'value':2})
G.add_node('C', attr_dict={'value':3})
G.add_node('D', attr_dict={'value':0})

# Populate edges 
G.add_edge('A','C', attr_dict={'math':'+'})
G.add_edge('B','C', attr_dict={'math':'-'})
G.add_edge('C','D', attr_dict={'math':'+'})

math_dict = nx.get_edge_attributes(G,'math')

# Order math dictionary for processing 

values = nx.get_node_attributes(G,'value')

# Calculation dictionary
calc_dict = {'+':np.add,
             '-':np.subtract,
             '*':np.multiply,
             '%':np.divide}

             
ancestors = nx.ancestors(G, 'C')

## Run colapse algorithm -- recursive 
# while values['D'] == 0: -- this doesn't work because the calc might not be finished 
# for loop doesn't work either because we keep injecting numbers
# is there a method to delete nodes once they have been calculated? -- Yes
# RuntimeError: dictionary changed size during iteration <--- SOLVE THIS! 

#i = 0
#for i in range(0,3):
#    print(i)
#    for key, math in math_dict.items():
#        val_list = [values[x] for x in key]
#        
#        if list(values.values()).count(0) == 1:
#            last = True
#        else:
#            last = False
#
#        if all(val_list) or last: # Onlly conduct calcultion if both values have been calculated or if the last set
#        # conduction calculation and update value 
#            values[key[1]] = calc_dict[math](*val_list)
#            math_dict.pop(key, math)
#    i += 1

# Recursive function     
def graph_colapse(math_dict):
    # List to remove 
    to_pop = {}
    
    for key, math in sorted(math_dict.items()):
        val_list = [values[x] for x in key]

        if list(values.values()).count(0) == 1:
            last = True
        else:
            last = False

        if all(val_list) or last:
            print('Processing: %s' %str(key))
            print('Values are: %s' %(val_list))
            print('Initial key value: %s = %s' %(key[1], values[key[1]]))
            
            values[key[1]] = calc_dict[math](*val_list)
            print('Updated key value: %s = %s' %(key[1], values[key[1]]))
            to_pop[key] = math

    # Remove
    for key, math in to_pop.items():
        math_dict.pop(key, math)
        
    return math_dict
    
while len(math_dict) > 0:
    print(math_dict.items())
    math_dict = graph_colapse(math_dict)

    
    
    
    
    
    
    
    
    
    
    
    
    
    