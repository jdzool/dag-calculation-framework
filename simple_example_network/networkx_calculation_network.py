#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:49:19 2017

@author: jondowning
"""
import networkx as nx
#import numpy as np
from networkx.drawing.nx_pydot import write_dot
import pygraphviz as pgv
#import pandas as pd 

# Load inputs! 

# Create a directed network 
# Calculations have a specific direction 
G = nx.DiGraph()

# Populate nodes and their values 
G.add_node('A', attr_dict={'value':5})
G.add_node('B', attr_dict={'value':2})
G.add_node('C', attr_dict={'value':3})
G.add_node('D', attr_dict={'value':4})
G.add_node('E', attr_dict={'value':0})

# Populate edges and their functions
G.add_edge('A','D', attr_dict={'math':'+'})
G.add_edge('B','D', attr_dict={'math':'-'})
G.add_edge('C','D', attr_dict={'math':'+'})
G.add_edge('D','E', attr_dict={'math':'+'})

# Create a dictionaries: one with values, the next with functions 
math_dict = nx.get_edge_attributes(G,'math')
values = nx.get_node_attributes(G,'value')


# Saving output and draw 
dot_path = "network.dot"

# Write .dot file to local drive 
write_dot(G,dot_path)

# Export visualisation 
# Edge attributes are not visualised but this is possible 
V = pgv.AGraph(dot_path)
V.layout(prog='dot')
V.draw('network.png')
V.draw('network.pdf')   


# TODO prove that a recursive function can operate in a network 
# We may have to understand the layers within the DAG for pygraphviz 