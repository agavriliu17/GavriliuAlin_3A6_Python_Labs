# Write a function that receives a variable number of sets and returns a dictionary 
# with the following operations from all sets two by two: reunion, intersection, a-b, b-a. 
# The key will have the following form: "a op b", where a and b are two sets,
# and op is the applied operator: |, &, -. 

def get_sets(*sets):
    result = {}
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            a = sets[i]
            b = sets[j]
            result[f"{a} | {b}"] = a.union(b)
            result[f"{a} & {b}"] = a.intersection(b)
            result[f"{a} - {b}"] = a.difference(b)
            result[f"{b} - {a}"] = b.difference(a)
    return result

def main():
    print(get_sets({1,2}, {2, 3}))

main()