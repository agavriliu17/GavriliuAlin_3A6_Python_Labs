import numpy as np
# Write a function that receives as a parameter a variable number of lists and 
# a whole number x. Return a list containing the items that appear exactly x times in the incoming lists. 

def x_times(*lists, x):
    arrays = np.concatenate(lists)
    uniqueArr = np.unique(arrays)
    result = []
    for i in uniqueArr:
        if np.count_nonzero(arrays == i) == x:
            result.append(i)
    return result

def main():
    print(x_times([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], x=2))

main()