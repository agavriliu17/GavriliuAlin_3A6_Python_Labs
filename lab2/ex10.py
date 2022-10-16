# Write a function that receives a variable number of lists and returns a list
# of tuples as follows: the first tuple contains the first items in the lists, 
# the second element contains the items on the position 2 in the lists, etc. 
# Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")]. 

def ordered(*lists):
    result = []
    for i in range(len(lists[0])):
        temp = []
        for j in range(len(lists)):
            temp.append(lists[j][i])
        result.append(tuple(temp))
    return result

def main():
    print(ordered([1,2,3], [5,6,7], ["a", "b", "c"]))

main()
