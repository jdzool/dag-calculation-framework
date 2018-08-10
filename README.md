# Calculation frameworks 

Numerical calculations can be defined in a graphical formats. Here graphical networks (networkx and pygraphviz) are used to store variables and functions on nodes and edges respectively. Calculations are then completed by collapsing each Directed Acyclic Graph (DAG)

## 1. Background 

When defining a calculation we start with a technical specification. This states inputs and outputs in terms of  their mathematical context. Each variable could be defined further as to set it belongs to (for example Real numbers).

<img src="https://github.com/jdvt/dag-calculation-framework/blob/master/readme_images/technical_specification.png" height="150" align="middle">

The implimentation of a calculation is completed using a computational tool. Loosely this is any framework that allows inputs and outputs joined through a chained mathematics. 

This could be through code: 

<p class="aligncenter">
<img src="https://github.com/jdvt/dag-calculation-framework/blob/master/readme_images/code_implementation.png" height="150">
</p>

Or by means of some graphical user interface that allows the appropriate inputs, for example Excel (and of course other tools exist!): 

<img src="https://github.com/jdvt/dag-calculation-framework/blob/master/readme_images/excel_implementation.png" align="middle" height="150">

Finally I propose that mixing the two to implement a calculation as a graphical network (below). Impliementing a calculation as pure code or purely in a graphical interface has various pros / cons. The benefits of using directed acyclic graphs is presented below. 

<img src="https://github.com/jdvt/dag-calculation-framework/blob/master/readme_images/graphical_network_implementation.png" height="150" align="middle">

## Calculation frameworks at Directed Acyclic Graphs

Using Directed Acyclic Graphs as a calculation framework has the following advantages:
**Feature** Calculations are self documenting: the code is the document and vice versa
**Benefit** 
* Calculations can be easily understood 
* Documentation is readily available 
* Documentation can be easily created as the calculations change 

**Feature** Calculations themselves are defined in code 
**Benefit** 
* Version control is possible 
* Each variable can be easily changed to allow for various types of analysis 
* Testability 

**Feature**  (variables are abstracted from formula)
**Benefit** 

**Downsides** 



## Functionality

Network defined in pygraphviz 
-- attributes given to nodes and edges 

Reduction / calculation is completed in networkx 
- Check on if inputs are inputs 

Plotting is completed in pygraphviz
- Plotting functionality is independent of calculation... But this could change.. 