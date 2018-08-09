# Recursive function     
def graph_colapse(math_dict, values_dict, calc_dict):
    # List to remove 
    to_pop = {}
    
    # Note: The order of mathematical functions is important  
    # This is a unique problem but has been solved 
    # Here simplistically we can use an alphabetical sort 
    # NB: we could use a topological sorting function here
    for key, math in sorted(math_dict.items()):
        val_list = [values_dict[x] for x in key]

        if list(values_dict.values()).count(0) == 1:
            last = True
        else:
            last = False

        if all(val_list) or last:
            print('Processing edge: %s' %str(key))
            print('Initial node value: %s = %s' %(key[0], values_dict[key[0]]))
            print('Node values are: %s' %(val_list))
            print('Edge function is %s' %math)
            
            values_dict[key[0]] = calc_dict[math](*val_list)
            print('Updated node value: %s = %s' %(key[0], values_dict[key[0]]))
            # Which items have been calculated 
            to_pop[key] = math

    # Remove edges which have been calculated 
    for key, math in to_pop.items():
        math_dict.pop(key, math)
        
    return math_dict